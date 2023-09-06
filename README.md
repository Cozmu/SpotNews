# Sejam bem-vindos ao projeto SpotNews!! 🗞️🔍

#### SpotNews é um protótipo de blog de notícias criado para fins de estudo. Desenvolvido com Django, MySQL e Django Rest Framework (DRF), este projeto demonstra as capacidades técnicas e práticas em desenvolvimento web. Embora não seja destinado à produção, oferece uma plataforma fictícia para acessar notícias e praticar habilidades de desenvolvimento.

## Tecnologias :

<ul>
  <li>Python</li>
  <li>Django</li>
  <li>Django Rest Framework (DRF)</li>
  <li>MySQL</li>
  <li>HTML</li>
</ul>

## Funcionalidades:

- Possível visualizar notícias.
- Possível visualizar detalhes de notícias.
- Possível adicionar novas noticias.
- Possível buscar notícias por categorias.

## Como executar:

- Clone em seu computador (via SHH).
- Abra um novo terminal em seu VSCode.
- Crie e ative o ambiente virtual com os seguintes comandos: 

    ```bash
    python3 -m venv .venv
    ```
    ```bash
    source .venv/bin/activate
    ```
- Baixe as dependências com:
    ```bash
    python3 -m pip install -r dev-requirements.txt
    ```
- Execute os comandos para criação e população das tabelas do banco de dados:
    ```bash
    python3 manage.py makemigrations
    ```
    ```bash
    python3 manage.py migrate
    ```
    ```bash
    python3 manage.py runscript seeds
    ```
- Rode o servidor com o seguinte comando:
    ```bash
    python3 manage.py runserver
    ```

## Como contribuir no projeto:
  1. Faça um **fork** do projeto;
  2. Crie uma nova branch com as suas alterações: `git checkout -b my-feature`;
  3. Salve as alterações e crie uma mensagem de commit contando o que você fez: `git commit -m "feature: My new feature"`;
  4. Envie as suas alterações: `git push origin my-feature`;
  5. Abra o seu pull-request na página do GitHub.<br><br>

## Licença:

 Esse projeto está sob a licença: 

 [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

 ##  Autor:

### <a href="https://www.linkedin.com/in/jorge-reis-dev/" ><b>Jorge Wellington.</b></a>
<a href="https://www.linkedin.com/in/jorge-reis-dev/" ></a>
