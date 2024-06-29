# PUC-Rio MVP Backend
![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)

Aplicação para consultar turmas disponíveis em uma escola de beach tennis e cadastras alunos.

# Iniciando

### Pre-requisitos

- python 3.11
- poetry
- Postgres

Esse projeto usa poetry para um melhor gerenciamento das dependências e o banco de dados Postgres:
`Poetry`: https://python-poetry.org/docs/
`Postgres`: https://www.postgresql.org/download/ or run a docker image of Postgres: https://hub.docker.com/_/postgres

### Instalação

Para inicializar um ambiente virtual `venv` no diretório e instalar as dependencias:

```
poetry install
```

Se não quiser usar o poetry:

```
pip install -r requirements.txt

```

### Carga Inicial dos dados

Após a instalação de uma instância do banco Postgres, crie um arquivo .env na raiz do diretório com as seguintes variáveis de ambiente necessárias para a conexão com o banco, substituindo os valores de usuário, senha, host, porta e nome do banco pelos presentes na sua instancia do banco:

```
POSTGRES_USER = "<seu_usuario>"
POSTGRES_PW = "<sua_senha>"
POSTGRES_URL = "<host>:<porta>/<nome_do_banco>"
```
Execute o comando `python carrega_db.py` ou `python3 carrega_db.py` para rodar o script python presente na raiz desse diretorio.


### Rodando a aplicação

Execute o comando
```
python app.py
```
no diretório raiz e acesse a documentação da aplicação pelo endereço `http://127.0.0.1:8000/openapi/swagger` no seu browser.
