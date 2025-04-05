--Criacao das tabelas do banco de dados

CREATE TABLE IF NOT EXISTS "alunos" (
  "nome"     varchar,
  "cpf"      varchar (11) PRIMARY KEY,
  "telefone" varchar (11),
  "endereco" varchar,
  "cep"      varchar(8),
  "data_nascimento" date,
  "email"    varchar
);

CREATE TABLE IF NOT EXISTS "professor" (
  "nome" varchar,
  "cpf" varchar(11) PRIMARY KEY,
  "telefone" varchar(11),
  "endereco" varchar,
  "cep"      varchar(8),
  "email" varchar,
  "data_nascimento" date,
  "informacoes_adicionais" varchar(5000)
);

CREATE TABLE IF NOT EXISTS "turma" (
  "id_turma" SERIAL PRIMARY KEY,
  "id_professor" varchar (11) NOT NULL,
  "nivel" varchar,
  "horario" time,
  "dia_semana" varchar,
  FOREIGN KEY ("id_professor") REFERENCES "professor" ("cpf")
);

CREATE TABLE IF NOT EXISTS "matricula" (
  "id_matricula" uuid PRIMARY KEY DEFAULT gen_random_uuid (),
  "id_aluno" varchar(11),
  "id_turma" integer,
  "data_matricula" date DEFAULT CURRENT_DATE,
  FOREIGN KEY ("id_aluno") REFERENCES "alunos" ("cpf"),
  FOREIGN KEY ("id_turma") REFERENCES "turma" ("id_turma"),
  UNIQUE ("id_aluno", "id_turma")
);
