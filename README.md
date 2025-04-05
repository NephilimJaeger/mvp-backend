# PUC-Rio MVP Backend
![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)

Aplicação para consultar turmas disponíveis em uma escola de beach tennis e cadastras alunos.

# Iniciando

### Pré-requisitos

Para executar este projeto, você precisará:

- Docker
- Docker Compose

Links para instalação:
- `Docker`: https://docs.docker.com/get-docker/
- `Docker Compose`: https://docs.docker.com/compose/install/

### Instalação

Primeiro, clone e abra o repositório:

```
git clone https://github.com/NephilimJaeger/mvp-backend.git
cd mvp-backend
```

### Usando Docker Compose

Esta opção configura automaticamente a aplicação e o banco de dados:

```
docker-compose up -d
```

O servidor estará disponível em `http://localhost:8000` e a documentação em `http://localhost:8000/openapi/swagger`

Para parar a aplicação:

```
docker-compose down
```

### Notas adicionais para Docker

- O banco de dados Postgres é configurado automaticamente
- Os dados iniciais são carregados automaticamente
- Todas as portas necessárias são mapeadas para o host
