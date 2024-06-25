from base import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import String, Date, Time
from datetime import date

class Pessoa(Base):
    __abstract__ = True
    nome = Column(String)
    cpf = Column(String(11), primary_key=True)
    telefone = Column(String)
    endereco = Column(String)
    email = Column(String)

class Aluno(Pessoa):
    __tablename__ = 'alunos'
    data_nascimento = Column(Date)
    data_inicio = Column(Date)

class Professor(Pessoa):
    __tablename__ = 'professores'
    especialidade = Column(String)
    informacoes_adicionais = Column(String)

class Turma(Base):
    __tablename__ = 'turma'
    id_turma = Column(String, primary_key=True)
    id_professor = Column(String), ForeignKey('professores.cpf')
    nível = Column(String)
    horário = Column(Time)
    dia_da_semana = Column(String)

class Inscricao(Base):
    __tablename__ = 'inscricao'
    id_inscricao = Column(String, primary_key=True)
    id_aluno = Column(String), ForeignKey('alunos.cpf')
    id_turma = Column(String), ForeignKey('turma.id_turma')
    data_inscricao = Column(Date, default=date.today().isoformat())

