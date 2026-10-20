"use strict";
document.documentElement.classList.add("js");
const menuButton = document.querySelector(".menu-button");
const navigation = document.querySelector("#navigation");
menuButton.hidden = false;
function closeMenu() {
  navigation.classList.remove("open");
  menuButton.setAttribute("aria-expanded", "false");
  menuButton.querySelector("span").textContent = "+";
}
menuButton.addEventListener("click", () => {
  const opened = navigation.classList.toggle("open");
  menuButton.setAttribute("aria-expanded", String(opened));
  menuButton.querySelector("span").textContent = opened ? "−" : "+";
});
navigation.addEventListener("click", (event) => {
  const link = event.target.closest("a");
  if (!link) return;
  const wasOpen = navigation.classList.contains("open");
  closeMenu();
  if (wasOpen) {
    const section = document.getElementById(link.hash.slice(1));
    if (section) {
      section.setAttribute("tabindex", "-1");
      section.focus({ preventScroll: true });
    }
  }
});
document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && navigation.classList.contains("open")) {
    closeMenu();
    menuButton.focus();
  }
});

const filters = document.querySelector(".project-filters");
filters.hidden = false;
const projectCards = [...document.querySelectorAll(".project-card")];
filters.addEventListener("click", (event) => {
  const selected = event.target.closest("[data-filter]");
  if (!selected) return;
  filters.querySelectorAll("button").forEach((button) => {
    button.classList.toggle("active", button === selected);
    button.setAttribute("aria-pressed", String(button === selected));
  });
  let count = 0;
  projectCards.forEach((card) => {
    const show = selected.dataset.filter === "all" || card.dataset.category === selected.dataset.filter;
    card.hidden = !show;
    if (show) count += 1;
  });
  document.querySelector("#filter-status").textContent = `${count} ${count === 1 ? "projeto exibido" : "projetos exibidos"}.`;
});

const copyButton = document.querySelector(".copy-email");
if (navigator.clipboard && window.isSecureContext) {
  copyButton.hidden = false;
  copyButton.addEventListener("click", async () => {
    const status = document.querySelector(".copy-status");
    try {
      await navigator.clipboard.writeText("souzastenio812@gmail.com");
      status.textContent = "E-mail copiado.";
    } catch {
      status.textContent = "Selecione o endereço acima para copiar.";
    }
  });
}

// A impressão sempre inclui todos os projetos e detalhes, mesmo após filtros.
let printState = null;
function preparePrint() {
  if (printState) return;
  const details = [...document.querySelectorAll("details")];
  printState = {
    details: details.map((element) => ({ element, open: element.open })),
    cards: projectCards.map((element) => ({ element, hidden: element.hidden })),
  };
  details.forEach((element) => { element.open = true; });
  projectCards.forEach((element) => { element.hidden = false; });
}
function restorePrint() {
  if (!printState) return;
  printState.details.forEach(({ element, open }) => { element.open = open; });
  printState.cards.forEach(({ element, hidden }) => { element.hidden = hidden; });
  printState = null;
}
document.querySelectorAll("[data-print]").forEach((button) => {
  button.hidden = false;
  button.addEventListener("click", () => { preparePrint(); window.print(); });
});
window.addEventListener("beforeprint", preparePrint);
window.addEventListener("afterprint", restorePrint);

if ("IntersectionObserver" in window) {
  const navLinks = [...navigation.querySelectorAll('a[href^="#"]')];
  const observer = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      navLinks.forEach((link) => {
        if (link.hash === `#${entry.target.id}`) link.setAttribute("aria-current", "location");
        else link.removeAttribute("aria-current");
      });
    }
  }, { rootMargin: "-15% 0px -60% 0px" });
  navLinks.forEach((link) => {
    const section = document.querySelector(link.hash);
    if (section) observer.observe(section);
  });
}
document.querySelector("[data-year]").textContent = new Date().getFullYear();
