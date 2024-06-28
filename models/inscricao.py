from sqlalchemy import Column, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import Date, String
from datetime import date
from models.base import Base


class Inscricao(Base):
    __tablename__ = "inscricao"
    id_inscricao = Column(
        UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid()
    )
    id_aluno = Column(String, ForeignKey("alunos.cpf"))
    id_turma = Column(String, ForeignKey("turma.id_turma"))
    data_inscricao = Column(Date, default=date.today)

    def __init__(self, id_aluno: str, id_turma: str, id_inscricao: UUID = None):
        self.id_inscricao = id_inscricao
        self.id_aluno = id_aluno
        self.id_turma = id_turma
        self.data_inscricao = date.today()
