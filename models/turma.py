from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import String, Time
from base import Base

class Turma(Base):
    __tablename__ = 'turma'
    id_turma = Column(String, primary_key=True)
    id_professor = Column(String, ForeignKey('professores.cpf'), nullable=False)
    nível = Column(String)
    horário = Column(Time)
    dia_da_semana = Column(String)

    def __init__(self, id_turma: str, id_professor: str, nível: str, horário: str, dia_da_semana: str):
        self.id_turma = id_turma
        self.id_professor = id_professor
        self.nível = nível
        self.horário = horário
        self.dia_da_semana = dia_da_semana