# Stênio Henrique de Souza — Portfólio

Portfólio profissional em português, com aplicações em Python, CLT Fácil, experiência, formação e competências.

**Site:** https://souzastenio812-byte.github.io/portfolio-stenio/

## Stack

HTML semântico, CSS responsivo e JavaScript nativo. Sem bibliotecas, fontes externas, rastreadores ou serviços de backend. O conteúdo permanece acessível sem JavaScript.

- Filtros de projetos por categoria.
- Diagramas de fluxo funcional (representações, não capturas dos aplicativos).
- Navegação móvel e por teclado.
- Preferência de movimento reduzido respeitada.
- Impressão com todos os projetos e responsabilidades, independentemente dos filtros.
- Metadados para mecanismos de busca e compartilhamento.

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

Nenhuma dependência adicional é necessária. O GitHub Pages serve o HTML já gerado; Python não é executado no servidor.

Os textos da apresentação, fluxos e entregas profissionais estão em `build.py`; o visual em `styles.css`; as interações em `app.js`.

## GitHub Pages

Configuração: **Settings → Pages → Deploy from a branch → main → / (root)**.
Os caminhos de CSS, JavaScript e retrato são relativos, compatíveis com o subdiretório do repositório.

## Conteúdo e privacidade

Informações baseadas no currículo e nos projetos descritos pelo autor. O retrato é o original fornecido. O PDF original do currículo, telefone, documentos e dados operacionais de clientes não fazem parte do repositório.

As imagens reais das aplicações poderão ser adicionadas posteriormente. Não há demonstrações inventadas ou botões que apontam para links inexistentes. O CLT Fácil tem links públicos; os demais projetos apresentam sua finalidade e fluxo.
