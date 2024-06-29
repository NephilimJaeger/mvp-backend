from sqlalchemy import Column, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import Date, String
from datetime import date
from models.base import Base


class Matricula(Base):
    __tablename__ = "matricula"
    id_matricula = Column(
        UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid()
    )
    id_aluno = Column(String, ForeignKey("alunos.cpf"))
    id_turma = Column(String, ForeignKey("turma.id_turma"))
    data_matricula = Column(Date, default=date.today)

    def __init__(self, id_aluno: str, id_turma: str, id_matricula: UUID = None):
        self.id_matricula = id_matricula
        self.id_aluno = id_aluno
        self.id_turma = id_turma
        self.data_matricula = date.today()
