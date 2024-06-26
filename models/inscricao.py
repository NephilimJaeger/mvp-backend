from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Date, String
from datetime import date
from base import Base

class Inscricao(Base):
    __tablename__ = 'inscricao'
    id_inscricao = Column(String, primary_key=True)
    id_aluno = Column(String), ForeignKey('alunos.cpf')
    id_turma = Column(String), ForeignKey('turma.id_turma')
    data_inscricao = Column(Date, default=date.today().isoformat())