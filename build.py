"""Gera HTML estático a partir de content.json. Requer apenas Python 3."""
import json
from html import escape as e
from pathlib import Path

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / "content.json").read_text(encoding="utf-8"))

def tags(items):
    return '<ul class="tags" aria-label="Tecnologias">' + "".join(f"<li>{e(x)}</li>" for x in items) + "</ul>"

flows = [
    [("01 / ENTRADA", "Tabelas da operação", "Dados de origem"),
     ("02 / PROCESSAMENTO", "Transformação em Python", "Preparação dos dados"),
     ("03 / SAÍDA", "Etiquetas de cliente", "Informação para a operação")],
    [("01 / ENTRADA", "Dados de embarque", "Informações da expedição"),
     ("02 / PROCESSAMENTO", "Geração automatizada", "Documentos + QR Code"),
     ("03 / SAÍDA", "Vias para conferência", "Leitura do QR Code")],
    [("01 / ENTRADA", "Leitura das etiquetas", "Bipagem"),
     ("02 / PROCESSAMENTO", "Batimento de dados", "Comparação em planilha"),
     ("03 / SAÍDA", "Conferência operacional", "Validação dos dados lidos")],
    [("01 / ENTRADA", "Dados informados", "Valores da simulação"),
     ("02 / PROCESSAMENTO", "Calculadora selecionada", "6 modalidades"),
     ("03 / SAÍDA", "Estimativa trabalhista", "Consulta educacional")],
]
project_cards = []
for i, app in enumerate(data["applications"]):
    links = ""
    if app.get("demoUrl"):
        links += f'<a class="button small primary" href="{e(app["demoUrl"],quote=True)}" target="_blank" rel="noopener noreferrer">Acessar site <span aria-hidden="true">↗</span></a>'
    if app.get("repositoryUrl"):
        links += f'<a class="text-link" href="{e(app["repositoryUrl"],quote=True)}" target="_blank" rel="noopener noreferrer">Código no GitHub <span aria-hidden="true">↗</span></a>'
    diagram = "".join(f'<div class="flow-step"><span class="micro">{e(n)}</span><strong>{e(title)}</strong><span>{e(desc)}</span></div>' for n,title,desc in flows[i])
    project_cards.append(f'''
    <article class="project-card" data-category="{"web" if i == 3 else "python"}">
      <div class="project-copy">
        <div class="project-top"><span class="project-number">0{i+1}</span><span class="micro">{"WEB / FERRAMENTA PÚBLICA" if i==3 else "PYTHON / AUTOMAÇÃO OPERACIONAL"}</span></div>
        <h3>{e(app["name"])}</h3>
        <p>{e(app["description"])}</p>
        {tags(app["technologies"])}
        <details class="project-details"><summary>Objetivo da solução <span aria-hidden="true">+</span></summary><p>{e(app["purpose"])}</p><p class="authorship">Desenvolvimento: Stênio Henrique de Souza.</p></details>
        {f'<div class="project-links">{links}</div>' if links else ""}
      </div>
      <div class="project-flow"><div class="flow-caption"><span class="status-dot" aria-hidden="true"></span> FLUXO FUNCIONAL</div><div class="flow-steps">{diagram}</div><span class="flow-note">Representação do funcionamento</span></div>
    </article>''')

experiences = []
for item in data["experiences"]:
    bullets = "".join(f"<li>{e(text)}</li>" for text in item["responsibilities"])
    experiences.append(f'''
    <article class="experience">
      <div class="experience-meta"><span class="mono">{e(item["period"])}</span>{'<span class="current">Atual</span>' if item["current"] else ''}</div>
      <div class="experience-body"><p class="company">{e(item["company"])}</p><h3>{e(item["role"])}</h3>
      <p>{e(item["responsibilities"][0])}</p>
      <details><summary>Responsabilidades e entregas <span aria-hidden="true">+</span></summary><ul class="responsibilities">{bullets}</ul></details></div>
    </article>''')

skill_cards = "".join(f'<article class="skill-card"><span class="micro">STACK / 0{i+1}</span><h3>{e(group["title"])}</h3>{tags(group["items"])}</article>' for i,group in enumerate(data["skills"]))
education = "".join(f'<article class="education-card"><span class="education-status">{"PREVISÃO" if item["status"]=="Cursando" else "CONCLUSÃO"} / {item["completionYear"]}</span><h3>{e(item["course"])}</h3><p>{e(item["school"])}</p><span class="course-state">{e(item["status"])}</span></article>' for item in data["education"])
courses = "".join(f'<li><span>{e(item["name"])}</span><span class="course-school">{e(item["institution"])}{f" · {item['year']}" if item.get("year") else ""}</span></li>' for item in data["courses"])
linkedin = e(data["contact"]["linkedin"], quote=True)

html = f'''<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="theme-color" content="#101716">
  <title>Stênio Henrique de Souza | Automação, Dados e TI</title>
  <meta name="description" content="Portfólio de Stênio Henrique de Souza: automações em Python, dados, sistemas e experiência em qualidade e logística. Conheça meus projetos e trajetória.">
  <link rel="canonical" href="https://souzastenio812-byte.github.io/portfolio-stenio/">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="pt_BR">
  <meta property="og:title" content="Stênio Henrique de Souza | Automação, Dados e TI">
  <meta property="og:description" content="Da rotina operacional à solução em código. Projetos em Python, desenvolvimento web e trajetória profissional.">
  <meta property="og:url" content="https://souzastenio812-byte.github.io/portfolio-stenio/">
  <meta property="og:image" content="https://souzastenio812-byte.github.io/portfolio-stenio/perfil.jpeg">
  <meta property="og:image:alt" content="Retrato de Stênio Henrique de Souza">
  <link rel="icon" href="./favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="./styles.css">
  <script src="./app.js" defer></script>
</head>
<body>
  <a class="skip-link" href="#conteudo">Pular para o conteúdo</a>
  <header class="site-header">
    <div class="header-inner">
      <a class="brand" href="#inicio" aria-label="Stênio Henrique, início"><span class="brand-symbol" aria-hidden="true">sh<span>_</span></span><span class="brand-label">STÊNIO HENRIQUE<span>PORTFÓLIO / 2026</span></span></a>
      <button class="menu-button" aria-expanded="false" aria-controls="navigation" hidden>Menu <span aria-hidden="true">+</span></button>
      <nav id="navigation" aria-label="Navegação principal">
        <a href="#projetos">Projetos<span>04</span></a><a href="#trajetoria">Trajetória</a><a href="#stack">Stack</a><a href="#formacao">Formação</a><a class="nav-contact" href="#contato">Contato <span aria-hidden="true">↗</span></a>
      </nav>
    </div>
  </header>
  <main id="conteudo">
    <section class="hero section-shell" id="inicio" aria-labelledby="hero-title">
      <div class="hero-copy">
        <p class="eyebrow"><span class="status-dot" aria-hidden="true"></span> QUALIDADE · LOGÍSTICA · TECNOLOGIA</p>
        <p class="hero-name">STÊNIO HENRIQUE DE SOUZA</p>
        <h1 id="hero-title">Da operação<br>ao <span>código.</span></h1>
        <p class="hero-description">Transformo rotinas operacionais em soluções com <strong>Python, dados e automação.</strong> Conecto a experiência em qualidade e logística à construção de ferramentas úteis no dia a dia.</p>
        <div class="hero-actions"><a class="button primary" href="#projetos">Explorar projetos <span aria-hidden="true">↘</span></a><a class="button secondary" href="#trajetoria">Ver trajetória <span aria-hidden="true">→</span></a></div>
        <div class="hero-location"><span aria-hidden="true">⌖</span> Varginha, MG <span class="separator">/</span> Foco em Suporte, TI e Sistemas</div>
      </div>
      <aside class="profile-card" aria-label="Apresentação profissional">
        <div class="panel-top"><span class="micro">PERFIL / STÊNIO HENRIQUE</span><span class="panel-dots" aria-hidden="true">● ● ●</span></div>
        <div class="portrait-wrap"><img src="./perfil.jpeg" alt="Retrato de Stênio Henrique de Souza" width="800" height="800" fetchpriority="high"><span class="portrait-corner top-left" aria-hidden="true"></span><span class="portrait-corner bottom-right" aria-hidden="true"></span><span class="portrait-caption mono">VARGINHA / MG</span></div>
        <div class="profile-info"><span class="micro">ATUAÇÃO ATUAL</span><strong>Analista Jr. de Qualidade e Logística</strong><span>DHL Supply Chain</span></div>
        <div class="profile-bottom"><span class="mono">Python · SQL · HTML</span><a href="https://github.com/souzastenio812-byte" target="_blank" rel="noopener noreferrer" aria-label="Perfil de Stênio no GitHub (abre em nova aba)">GitHub <span aria-hidden="true">↗</span></a></div>
      </aside>
    </section>
    <div class="signal-strip section-shell" aria-label="Áreas de atuação"><span class="micro">DA ROTINA À SOLUÇÃO</span><span>01 <strong>Entender o processo</strong></span><span class="signal-arrow" aria-hidden="true">→</span><span>02 <strong>Trabalhar os dados</strong></span><span class="signal-arrow" aria-hidden="true">→</span><span>03 <strong>Automatizar a execução</strong></span></div>

    <section class="section-shell about section-block" id="sobre" aria-labelledby="sobre-title">
      <div class="section-label"><span>01 / CONTEXTO</span><span class="fine-rule"></span></div>
      <div class="about-grid"><h2 id="sobre-title">Tecnologia com <br><span class="muted">contexto de operação.</span></h2><div><p>Minha trajetória passa por qualidade, logística e sistemas corporativos. É nesse contato com processos reais que encontro oportunidades para organizar dados, melhorar conferências e automatizar tarefas.</p><p>Tenho formação técnica em Redes de Computadores e curso Análise e Desenvolvimento de Sistemas e Gestão da Qualidade. Direciono meu desenvolvimento profissional para <strong>Suporte, TI e Sistemas</strong>, com projetos em Python e experiência com indicadores e ERPs.</p><a class="text-link" href="#stack">Conheça minhas competências <span aria-hidden="true">→</span></a></div></div>
    </section>

    <section class="projects section-block section-shell" id="projetos" aria-labelledby="projects-title">
      <div class="section-label"><span>02 / PROJETOS</span><span class="fine-rule"></span><span>04 SOLUÇÕES</span></div>
      <div class="section-heading"><div><h2 id="projects-title">Aplicações que desenvolvi<span class="accent">.</span></h2><p>Ferramentas construídas a partir de necessidades concretas.</p></div><div class="project-filters" role="group" aria-label="Filtrar projetos" hidden><button class="filter active" data-filter="all" aria-pressed="true">Todos <span>04</span></button><button class="filter" data-filter="python" aria-pressed="false">Python <span>03</span></button><button class="filter" data-filter="web" aria-pressed="false">Web <span>01</span></button></div></div>
      <p class="sr-only" id="filter-status" role="status" aria-live="polite"></p>
      <div class="project-list">{"".join(project_cards)}</div>
    </section>

    <section class="impact section-block section-shell" id="entregas" aria-labelledby="impact-title">
      <div class="section-label"><span>03 / ENTREGAS PROFISSIONAIS</span><span class="fine-rule"></span></div>
      <h2 id="impact-title">Processos, sistemas e resultado.</h2>
      <div class="impact-grid">
        <article class="impact-card"><span class="micro">DHL SUPPLY CHAIN / QUALIDADE</span><div class="impact-number">&gt;75<span>%</span></div><h3>Redução nas devoluções por avarias</h3><p>Implantação de fluxo de inspeção, com critérios, documentação e treinamentos na operação logística. Mais precisão nas conferências e padronização no SGQ.</p><span class="impact-foot">Resultado registrado no currículo profissional</span></article>
        <article class="impact-card erp-card"><span class="micro">PP PRINT / SISTEMAS CORPORATIVOS</span><div class="erp-visual" aria-label="TOTVS Protheus: Inspeção de Entrada e MRP"><span class="erp-root">TOTVS Protheus</span><div><span>Inspeção de Entrada</span><span>MRP</span></div></div><h3>Participação na implementação de módulos</h3><p>Estruturação e cadastro de dados, testes, parametrizações e controles para apoiar a operação nos módulos de Inspeção de Entrada e MRP.</p><span class="impact-foot">Integração entre dados, qualidade e produção</span></article>
      </div>
    </section>

    <section class="section-block section-shell" id="trajetoria" aria-labelledby="career-title">
      <div class="section-label"><span>04 / EXPERIÊNCIA</span><span class="fine-rule"></span></div>
      <div class="section-heading"><div><h2 id="career-title">Uma trajetória construída na prática.</h2><p>Da operação logística à análise de qualidade e desenvolvimento de soluções.</p></div><button class="text-link print-button" data-print hidden>Salvar currículo em PDF <span aria-hidden="true">↗</span></button></div>
      <div class="timeline">{"".join(experiences)}</div>
    </section>

    <section class="section-block section-shell" id="stack" aria-labelledby="stack-title">
      <div class="section-label"><span>05 / COMPETÊNCIAS</span><span class="fine-rule"></span></div>
      <div class="section-heading"><div><h2 id="stack-title">Meu repertório técnico.</h2><p>Desenvolvimento, dados, infraestrutura e sistemas corporativos.</p></div><span class="mono section-aside">ferramentas + conhecimento de processo</span></div>
      <div class="skills-grid">{skill_cards}</div>
    </section>

    <section class="section-block section-shell" id="formacao" aria-labelledby="education-title">
      <div class="section-label"><span>06 / FORMAÇÃO</span><span class="fine-rule"></span></div>
      <h2 id="education-title">Aprendizado em evolução.</h2><div class="education-grid">{education}</div>
      <div class="courses"><h3>Cursos complementares</h3><ul>{courses}</ul></div>
    </section>

    <section class="contact section-shell section-block" id="contato" aria-labelledby="contact-title">
      <div class="section-label"><span>07 / CONTATO</span><span class="fine-rule"></span></div>
      <div class="contact-grid"><div><p class="eyebrow">SUPORTE · TI · SISTEMAS</p><h2 id="contact-title">Vamos conversar<br>sobre <span>tecnologia?</span></h2><p>Para oportunidades profissionais ou uma conversa sobre meus projetos.</p></div><div class="contact-links"><a class="contact-email" href="mailto:souzastenio812@gmail.com"><span class="micro">E-MAIL</span><strong>souzastenio812@gmail.com</strong><span aria-hidden="true">↗</span></a><div class="social-links"><a href="{linkedin}" target="_blank" rel="noopener noreferrer">LinkedIn <span aria-hidden="true">↗</span></a><a href="https://github.com/souzastenio812-byte" target="_blank" rel="noopener noreferrer">GitHub <span aria-hidden="true">↗</span></a><button class="copy-email" hidden>Copiar e-mail <span aria-hidden="true">⧉</span></button></div><p class="copy-status" role="status" aria-live="polite"></p></div></div>
    </section>
  </main>
  <footer class="footer section-shell"><span>© <span data-year>2026</span> Stênio Henrique de Souza</span><span class="mono">Processos reais. Soluções em código.</span><a href="#inicio">Voltar ao topo <span aria-hidden="true">↑</span></a></footer>
</body>
</html>'''
(ROOT / "index.html").write_text(html, encoding="utf-8")
print("index.html gerado com 4 projetos e currículo completo.")
