# Stênio Henrique de Souza — Portfólio

Portfólio profissional em português, com aplicações em Python, CLT Fácil, experiência, formação e competências.

**Site:** https://souzastenio812-byte.github.io/portfolio-stenio/

## Stack

HTML semântico, CSS responsivo e JavaScript nativo. Sem bibliotecas, fontes externas, rastreadores ou serviços de backend. O conteúdo permanece acessível sem JavaScript.

- Filtros de projetos por categoria.
- Análise de cada projeto: contexto, solução e entrega.
- Diagramas de fluxo funcional (representações, não capturas dos aplicativos).
- Navegação móvel e por teclado.
- Preferência de movimento reduzido respeitada.
- Impressão com todos os projetos e responsabilidades, independentemente dos filtros.
- Metadados para mecanismos de busca e compartilhamento.
- Dados estruturados ProfilePage/Person com cargo e empresa reais.

## Desenvolvimento local

Execute na pasta do projeto:

```sh
python -m http.server 8765 --bind 127.0.0.1
```

Abra http://127.0.0.1:8765/. Também é possível abrir `index.html` diretamente.

## Editar conteúdo

O arquivo `content.json` concentra dados do currículo e das aplicações. `build.py` utiliza esses dados e os textos de apresentação para gerar `index.html`:

```sh
python build.py
```

Requer Python 3.12 ou superior, sem dependências adicionais. O GitHub Pages serve o HTML já gerado; Python não é executado no servidor.

Cada aplicação em `content.json` tem um `id` único, categoria `kind` (`python` ou `web`), tecnologias, fluxo `flow` e análise `case` com `context`, `solution` e `delivery`. A ordem dos projetos pode ser alterada sem trocar os fluxos ou categorias. Os contadores são calculados automaticamente. Links de site e repositório são opcionais e devem usar HTTPS.

Os textos de apresentação e entregas profissionais estão em `build.py`; os componentes de projetos e dados estruturados em `site_components.py`; o visual em `styles.css`; as interações em `app.js`.

Para incluir uma captura real, coloque a imagem no projeto, por exemplo `images/etiquetas.webp`, e acrescente ao objeto da aplicação:

```json
"image": {
  "src": "images/etiquetas.webp",
  "alt": "Tela da aplicação de etiquetas preenchida com dados de exemplo",
  "caption": "Geração de etiquetas de cliente"
}
```

Use somente capturas autorizadas, com dados de exemplo. O texto alternativo é obrigatório. Gere novamente `index.html` após editar o conteúdo.

## Verificação

```sh
python build.py
python -m unittest -v
node --check app.js
```

Os testes cobrem reordenação e inclusão de projetos, escape de HTML, validação de links e imagens, dados estruturados, âncoras, arquivos locais e estrutura básica do documento. Node é necessário apenas para a verificação opcional da sintaxe JavaScript.

O workflow `.github/workflows/ci.yml` executa essas verificações em pushes para `main`, pull requests e execução manual. Também verifica se `index.html` foi regenerado após alterações. Usa acesso de leitura ao repositório, sem segredos.

## GitHub Pages

Configuração: **Settings → Pages → Deploy from a branch → main → / (root)**.
Os caminhos de CSS, JavaScript e retrato são relativos, compatíveis com o subdiretório do repositório.

O workflow de verificação informa falhas; a publicação por branch do GitHub Pages ocorre separadamente. Antes de publicar, execute as verificações locais. Para reverter uma atualização, restaure a versão anterior dos arquivos pelo histórico de commits.

## Conteúdo e privacidade

Informações baseadas no currículo e nos projetos descritos pelo autor. O retrato é o original fornecido. O WhatsApp profissional foi incluído por solicitação do autor. O PDF original do currículo, documentos e dados operacionais de clientes não fazem parte do repositório.

As imagens reais das aplicações poderão ser adicionadas posteriormente. Não há demonstrações inventadas ou botões que apontam para links inexistentes. O CLT Fácil tem links públicos; os demais projetos apresentam sua finalidade e fluxo.

As descrições das aplicações de etiquetas e vias de exportação foram detalhadas a partir dos scripts fornecidos pelo autor. O curso de Inteligência Artificial no Bradesco, em parceria com o Google, foi informado como concluído; o título oficial, a carga horária e a data do certificado não foram fornecidos.
