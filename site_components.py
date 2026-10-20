"""Componentes estáticos do portfólio. Apenas biblioteca padrão Python."""
import json
import re
from html import escape
from pathlib import PurePosixPath
from urllib.parse import urlsplit


def https_link(value):
    """Rejeita protocolos executáveis, credenciais e URLs malformadas."""
    if not value:
        return None
    if not isinstance(value, str) or any(char.isspace() for char in value):
        raise ValueError("O link deve ser uma URL HTTPS sem espaços.")
    try:
        parsed = urlsplit(value)
        valid_port = parsed.port in (None, 443)
    except ValueError as error:
        raise ValueError("URL inválida.") from error
    if (parsed.scheme != "https" or not parsed.hostname or parsed.username
            or parsed.password or "\\" in value or not valid_port):
        raise ValueError("Use um link público HTTPS, sem credenciais.")
    return value


def local_image(value):
    """As capturas devem estar no projeto e usar um caminho relativo."""
    if not isinstance(value, str):
        raise ValueError("O caminho da imagem deve ser texto.")
    path = PurePosixPath(value)
    if (not value or "\\" in value or ":" in value or path.is_absolute()
            or ".." in path.parts or path.suffix.lower() not in
            (".png", ".jpg", ".jpeg", ".webp", ".avif")):
        raise ValueError("Use uma imagem local com caminho relativo.")
    return value


def tags(items):
    return '<ul class="tags" aria-label="Tecnologias">' + "".join(
        f"<li>{escape(item)}</li>" for item in items
    ) + "</ul>"


def project_counts(applications):
    return {kind: sum(app["kind"] == kind for app in applications)
            for kind in ("python", "web")} | {"all": len(applications)}


def render_projects(applications, author):
    cards = []
    seen = set()
    for index, app in enumerate(applications, 1):
        slug, kind = app["id"], app["kind"]
        if not re.fullmatch(r"[a-z][a-z0-9-]*", slug) or slug in seen:
            raise ValueError("Cada projeto precisa de um id único em minúsculas.")
        if kind not in ("python", "web"):
            raise ValueError("Categoria de projeto desconhecida.")
        if not app["flow"]:
            raise ValueError("O fluxo do projeto não pode estar vazio.")
        seen.add(slug)
        title = escape(app["name"])
        links = []
        for key, label, style in (
            ("demoUrl", "Acessar site", "button small primary"),
            ("repositoryUrl", "Código no GitHub", "text-link"),
        ):
            url = https_link(app.get(key))
            if url:
                links.append(
                    f'<a class="{style}" href="{escape(url, quote=True)}" '
                    f'target="_blank" rel="noopener noreferrer">{label}'
                    '<span class="sr-only"> (abre em nova aba)</span>'
                    ' <span aria-hidden="true">↗</span></a>'
                )
        flow = "".join(
            '<li class="flow-step">'
            f'<span class="micro">{escape(step["label"])}</span>'
            f'<strong>{escape(step["title"])}</strong>'
            f'<span>{escape(step["description"])}</span></li>'
            for step in app["flow"]
        )
        case = "".join(
            f'<div><dt>{label}</dt><dd>{escape(app["case"][key])}</dd></div>'
            for key, label in (("context", "Contexto"), ("solution", "Solução"),
                               ("delivery", "Entrega"))
        )
        screenshot = ""
        if app.get("image"):
            img = app["image"]
            src = local_image(img["src"])
            if not img.get("alt", "").strip():
                raise ValueError("A captura do projeto precisa de texto alternativo.")
            screenshot = (
                '<figure class="project-screenshot">'
                f'<img src="./{escape(src, quote=True)}" '
                f'alt="{escape(img["alt"], quote=True)}" loading="lazy" decoding="async">'
                f'<figcaption>{escape(img.get("caption", "Captura da aplicação"))}</figcaption>'
                '</figure>'
            )
        category = "WEB / FERRAMENTA PÚBLICA" if kind == "web" else "PYTHON / AUTOMAÇÃO OPERACIONAL"
        cards.append(f'''
    <article class="project-card" id="projeto-{slug}" data-category="{kind}" aria-labelledby="title-{slug}">
      <div class="project-copy">
        <div class="project-top"><span class="project-number" aria-hidden="true">{index:02d}</span><span class="micro">{category}</span></div>
        <h3 id="title-{slug}">{title}</h3>
        <p>{escape(app["description"])}</p>
        {tags(app["technologies"])}
        <details class="project-details">
          <summary>Ver análise técnica<span class="sr-only"> de {title}</span><span aria-hidden="true">+</span></summary>
          <dl class="case-details">{case}</dl>
          {screenshot}
          <p class="authorship">Desenvolvimento: {escape(author)}.</p>
        </details>
        {f'<div class="project-links">{"".join(links)}</div>' if links else ""}
      </div>
      <figure class="project-flow">
        <figcaption class="flow-caption"><span class="status-dot" aria-hidden="true"></span> FLUXO FUNCIONAL</figcaption>
        <ol class="flow-steps">{flow}</ol><p class="flow-note">Representação do funcionamento</p>
      </figure>
    </article>''')
    return "".join(cards)


def profile_schema(contact, current_role, site_url):
    github = https_link(contact["github"])
    linkedin = https_link(contact["linkedin"])
    schema = {
        "@context": "https://schema.org",
        "@type": "ProfilePage",
        "@id": site_url + "#perfil",
        "url": site_url,
        "name": contact["name"] + " | Automação, Dados e TI",
        "inLanguage": "pt-BR",
        "mainEntity": {
            "@type": "Person",
            "@id": site_url + "#pessoa",
            "name": contact["name"],
            "url": site_url,
            "image": site_url + "perfil.jpeg",
            "jobTitle": current_role["role"],
            "worksFor": {"@type": "Organization", "name": current_role["company"]},
            "sameAs": [github, linkedin],
        },
    }
    # Impede que conteúdo JSON possa encerrar o elemento script.
    return json.dumps(schema, ensure_ascii=False).replace("<", "\\u003c")
