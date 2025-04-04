# PUC-Rio MVP Backend
![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)

Aplicação para consultar turmas disponíveis em uma escola de beach tennis e cadastras alunos.

# Iniciando

### Pre-requisitos

#### Opção 1 (Recomendada): Docker

- Docker
- Docker Compose

#### Opção 2: Instalação Manual

- Python 3.11
- poetry ou venv
- Postgres

Esse projeto usa Docker para facilitar a configuração, mas também suporta instalação manual via Poetry ou venv. Se você optar pela instalação manual, precisa instalar uma instância do Postgres:
`Docker`: https://docs.docker.com/get-docker/
`Docker Compose`: https://docs.docker.com/compose/install/
`Poetry`: https://python-poetry.org/docs/
`Postgres`: https://www.postgresql.org/download/ or run a docker image of Postgres: https://hub.docker.com/_/postgres

### Instalação

Primeiro, clone e abra o repositório:

```
git clone https://github.com/NephilimJaeger/mvp-backend.git
cd mvp-backend
```
Em seguida, instale as depências em um ambiente virtual:

#### Opção 1:Usando Docker Compose (Recomendado)

Esta opção configura automaticamente a aplicação e o banco de dados:

```
docker-compose up -d
```

O servidor estará disponível em `http://localhost:8000` e a documentação em `http://localhost:8000/openapi/swagger`

Para parar a aplicação:

```
docker-compose down
```

#### Opção 2: Instalação Manual

##### Usando Poetry

Se você não estiver em um ambiente virtual, o poetry cria um automaticamente

```
poetry install
```

##### Sem usar Poetry

Mac/Linux

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Windows
```
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

#### Carga Inicial dos dados

Após a instalação de uma instância do banco Postgres, crie um arquivo .env na raiz do diretório com as seguintes variáveis de ambiente necessárias para a conexão com o banco, substituindo os valores de usuário, senha, host, porta e nome do banco pelos presentes na sua instancia do banco:

```
POSTGRES_USER = "<seu_usuario>"
POSTGRES_PW = "<sua_senha>"
POSTGRES_URL = "<host>:<porta>/<nome_do_banco>"
```
Execute o comando `python carrega_db.py` ou `python3 carrega_db.py` para rodar o script python presente na raiz desse diretorio.


#### Rodando a aplicação manualmente

Execute o comando
```
python app.py
```
no diretório raiz e acesse a documentação da aplicação pelo endereço `http://127.0.0.1:8000/openapi/swagger` no seu browser.

### Notas adicionais para Docker

- O banco de dados Postgres é configurado automaticamente
- Os dados iniciais são carregados automaticamente
- Todas as portas necessárias são mapeadas para o host
