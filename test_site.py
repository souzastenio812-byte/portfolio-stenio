"""Regressões de conteúdo, links e geração. Execute: python -m unittest -v."""
import copy
import json
import unittest
from html.parser import HTMLParser
from pathlib import Path

from site_components import https_link, local_image, profile_schema, render_projects

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / "content.json").read_text(encoding="utf-8"))


class Document(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.ids = []
        self.anchors = []
        self.assets = []
        self.images = []
        self.headings = []
        self.lang = None
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.append(attrs["id"])
        if tag == "html":
            self.lang = attrs.get("lang")
        if tag == "h1":
            self.headings.append(tag)
        if tag == "img":
            self.images.append(attrs)
        href = attrs.get("href", "")
        if href.startswith("#"):
            self.anchors.append(href[1:])
        if tag in ("img", "script", "link"):
            path = attrs.get("src", attrs.get("href", ""))
            if path.startswith("./"):
                self.assets.append(path)


class ProjectRegressionTests(unittest.TestCase):
    def test_order_and_addition_do_not_change_project_categories_or_flows(self):
        apps = copy.deepcopy(list(reversed(DATA["applications"])))
        extra = copy.deepcopy(apps[0])
        extra["id"] = "novo-projeto"
        extra["name"] = "Novo projeto"
        apps.append(extra)
        rendered = render_projects(apps, DATA["contact"]["name"])
        for app in apps:
            card = rendered.split(f'id="projeto-{app["id"]}"', 1)[1].split("</article>", 1)[0]
            self.assertIn(f'data-category="{app["kind"]}"', card)
            self.assertIn(app["flow"][0]["title"], card)

    def test_unsafe_links_are_rejected_instead_of_rendered(self):
        for value in ("javascript:alert(1)", "data:text/html,test", "//example.com",
                      "http://example.com", "https://user:secret@example.com",
                      "https://example.com\\@bad.test", "https://example.com bad",
                      "https://example.com:invalid", "https://"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                https_link(value)
        self.assertEqual(https_link("https://example.com/app?q=1&view=2"),
                         "https://example.com/app?q=1&view=2")
        self.assertIsNone(https_link(""))

    def test_missing_links_do_not_create_empty_buttons(self):
        app = copy.deepcopy(DATA["applications"][0])
        app.pop("demoUrl", None)
        app.pop("repositoryUrl", None)
        self.assertNotIn("project-links", render_projects([app], "Autor"))

    def test_html_in_content_is_escaped(self):
        app = copy.deepcopy(DATA["applications"][0])
        app["name"] = "<script>alert(1)</script>"
        html = render_projects([app], '<b>Autor</b>')
        self.assertNotIn("<script>", html)
        self.assertIn("&lt;script&gt;", html)
        self.assertNotIn("<b>Autor</b>", html)

    def test_duplicate_project_ids_fail_with_clear_error(self):
        app = DATA["applications"][0]
        with self.assertRaisesRegex(ValueError, "id único"):
            render_projects([app, app], "Autor")

    def test_project_images_stay_local_and_require_alt(self):
        for value in ("../private.jpeg", "/private.jpeg", "https://example.com/a.jpg",
                      "C:\\private.jpg", "images/a.svg"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                local_image(value)
        self.assertEqual(local_image("images/app.webp"), "images/app.webp")
        app = copy.deepcopy(DATA["applications"][0])
        app["image"] = {"src": "images/app.png", "alt": ""}
        with self.assertRaisesRegex(ValueError, "texto alternativo"):
            render_projects([app], "Autor")

    def test_json_ld_cannot_close_script_and_keeps_real_current_role(self):
        contact = copy.deepcopy(DATA["contact"])
        contact["name"] = "</script><script>alert(1)</script>"
        text = profile_schema(contact, DATA["experiences"][0], DATA["siteUrl"])
        self.assertNotIn("</script>", text)
        self.assertEqual(json.loads(text)["mainEntity"]["name"], contact["name"])
        self.assertEqual(json.loads(text)["mainEntity"]["jobTitle"],
                         DATA["experiences"][0]["role"])


class PublishedDocumentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.document = Document((ROOT / "index.html").read_text(encoding="utf-8"))

    def test_anchors_have_unique_existing_targets(self):
        self.assertEqual(len(self.document.ids), len(set(self.document.ids)))
        self.assertFalse(set(self.document.anchors) - set(self.document.ids))

    def test_local_assets_exist_and_images_have_alternatives(self):
        for path in self.document.assets:
            with self.subTest(path=path):
                self.assertTrue((ROOT / path).is_file())
        self.assertTrue(self.document.images)
        for image in self.document.images:
            self.assertTrue(image.get("alt", "").strip())

    def test_primary_language_and_heading_are_present(self):
        self.assertEqual(self.document.lang, "pt-BR")
        self.assertEqual(len(self.document.headings), 1)


if __name__ == "__main__":
    unittest.main()
