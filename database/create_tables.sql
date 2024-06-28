--Criacao das tabelas do banco de dados

CREATE TABLE IF NOT EXISTS "alunos" (
  "nome"     varchar,
  "cpf"      varchar (11) PRIMARY KEY,
  "telefone" varchar (11),
  "endereco" varchar,
  "data_nascimento" date,
  "email"    varchar
);

CREATE TABLE IF NOT EXISTS "professor" (
  "nome" varchar,
  "cpf" varchar(11) PRIMARY KEY,
  "telefone" varchar(11),
  "endereco" varchar,
  "email" varchar,
  "informacoes_adicionais" varchar
);

CREATE TABLE IF NOT EXISTS "turma" (
  "id_turma" SERIAL PRIMARY KEY,
  "id_professor" varchar (11) NOT NULL,
  "nivel" varchar,
  "horario" time,
  "dia_semana" varchar,
  FOREIGN KEY ("id_professor") REFERENCES "professor" ("cpf")
);

CREATE TABLE IF NOT EXISTS "inscricao" (
  "id_inscricao" uuid PRIMARY KEY DEFAULT gen_random_uuid (),
  "id_aluno" varchar(11),
  "id_turma" integer,
  "data_inscricao" date,
  FOREIGN KEY ("id_aluno") REFERENCES "alunos" ("cpf"),
  FOREIGN KEY ("id_turma") REFERENCES "turma" ("id_turma"),
  UNIQUE ("id_aluno", "id_turma")
);