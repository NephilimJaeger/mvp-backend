--Criacao das tabelas do banco de dados

CREATE TABLE "alunos" (
  "nome"     varchar,
  "cpf"      varchar (11) PRIMARY KEY,
  "telefone" varchar (11),
  "endereco" varchar,
  "data_nascimento" date,
  "email"    varchar,
  "data_inicio" date
);

CREATE TABLE "professor" (
  "nome" varchar,
  "cpf" varchar(11) PRIMARY KEY,
  "telefone" varchar(11),
  "endereco" varchar,
  "email" varchar,
  "especialidade" varchar
);

CREATE TABLE "turma" (
  "id_turma" integer PRIMARY KEY,
  "id_professor" varchar (11),
  "nivel" varchar,
  "horário" time,
  "dia_semana" varchar,
  FOREIGN KEY ("id_professor") REFERENCES "professor" ("cpf")
);

CREATE TABLE "inscricao" (
  "id_inscricao" varchar PRIMARY KEY,
  "id_aluno" varchar(11),
  "id_turma" integer,
  "data_incricao" date,
  FOREIGN KEY ("id_aluno") REFERENCES "alunos" ("cpf"),
  FOREIGN KEY ("id_turma") REFERENCES "turma" ("id_turma")
);