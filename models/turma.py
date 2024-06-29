from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import String, Time, Integer
from typing import Optional
from models.base import Base


class Turma(Base):
    __tablename__ = "turma"
    id_turma = Column(Integer, primary_key=True, autoincrement=True)
    id_professor = Column(String, ForeignKey("professores.cpf"), nullable=False)
    nivel = Column(String)
    horario = Column(Time)
    dia_semana = Column(String)

    def __init__(
        self,
        id_professor: str,
        nivel: str,
        horario: str,
        dia_semana: str,
        id_turma: Optional[int] = None,
    ):
        self.id_turma = id_turma
        self.id_professor = id_professor
        self.nivel = nivel
        self.horario = horario
        self.dia_semana = dia_semana
