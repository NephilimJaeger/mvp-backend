from pydantic import BaseModel

class Aluno(BaseModel):
    nome: str

class Professor(BaseModel):
    nome: str
    informacoes_adicionais: str

class Turma(BaseModel):
    horario: str
    professor: Professor
    dia_da_semana: str