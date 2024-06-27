from pydantic import BaseModel, Field
from models import Turma, Professor
from sqlalchemy.orm.session import Session
from datetime import time


class TurmaDisplay(BaseModel):
    id_turma: int = Field(..., description="Identificador da turma")
    horario: str = Field(..., description="Horário da turma")
    professor: str = Field(..., description="Nome do professor")
    nivel: str = Field(..., description="Nível da turma")
    dia_semana: str = Field(..., description="Dia da semana em que a aula ocorre")


def mostra_turmas(lista_turmas: list[Turma], session: Session):
    turmas = []
    for turma in lista_turmas:
        professor = (
            session.query(Professor).filter(Professor.cpf == turma.id_professor).first()
        )
        nome_professor = professor.nome if professor else "Sem professor cadastrado"
        turmas.append(
            {
                "id_turma": turma.id_turma,
                "horario": turma.horario.strftime("%H:%M:%S"),
                "professor": nome_professor,
                "nivel": turma.nivel,
                "dia_semana": turma.dia_semana,
            }
        )
    return {"turmas": turmas}
