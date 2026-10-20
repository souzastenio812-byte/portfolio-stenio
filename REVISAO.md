# Revisão técnica — 20/10/2026

## Alterações

- Projetos com contexto, solução e entrega, a partir das informações fornecidas pelo autor.
- Fluxos, categorias e contadores ligados aos dados de cada aplicação, sem depender de sua posição na lista.
- Campo opcional para capturas reais, com texto alternativo obrigatório.
- Tipografia maior, controles principais com área de toque de pelo menos 44 px de altura e navegação móvel com transferência de foco ao destino.
- Nome do profissional no título principal e dados estruturados ProfilePage/Person.
- Remoção da repetição da primeira responsabilidade nas experiências.
- Validação de links HTTPS, escape de texto e rejeição de caminhos inadequados para imagens.
- Testes automatizados e workflow de verificação com permissão de leitura.

## Evidências locais

- Geração do HTML e 10 testes Python aprovados.
- Sintaxe JavaScript validada com `node --check`.
- Filtros: três projetos Python, um Web e quatro no total.
- Abertura da análise técnica por Enter.
- Menu móvel: seleção transfere foco para a seção; Escape fecha o menu e devolve o foco ao botão.
- Sem rolagem horizontal nas larguras de viewport de 1280, 390 e 320 px.
- Na versão de teste sem o script da aplicação, navegação e quatro projetos permanecem disponíveis.
- Retrato carregado na prévia e ausência de erros ou avisos no console durante a verificação.
- Contraste calculado para as principais combinações de texto: 7,64:1 a 14,79:1. Texto secundário sobre painel: 7,64:1; botão principal: 13,33:1.

Essa revisão é limitada aos itens acima. Não equivale a uma certificação de acessibilidade, auditoria com leitores de tela ou garantia de posicionamento em buscas. A impressão mantém o suporte existente; a paginação física não foi revalidada nesta revisão.

## Diretrizes aplicadas

Skills locais: `portfolio-e-cases-para-atrair-clientes`, `design-de-case-study-visual`, `curriculocv-otimizado`, `acessibilidade-web-wcag-checklist`, `code-review-estruturado-checklist`, `auditoria-de-seo-on-page`, `checklist-de-entrega-de-projeto-dev` e `pipeline-cicd-github-actions`.

Os procedimentos foram adaptados a um portfólio profissional estático. As descrições não atribuem bibliotecas, métricas ou resultados não confirmados pelo autor. As capturas das aplicações ainda serão fornecidas.

Referências: [ProfilePage no Google Search](https://developers.google.com/search/docs/appearance/structured-data/profile-page), [actions/checkout](https://github.com/actions/checkout) e [actions/setup-python](https://github.com/actions/setup-python).
