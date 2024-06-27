from pydantic import BaseModel, Field
from models import Inscricao
from sqlalchemy.orm.session import Session
from schemas import AlunoBase
from datetime import date

class InscricaoBase(BaseModel):
    dados_aluno: AlunoBase
    id_turma: int
    data_inscricao: date = Field(date.today(), description="Data da inscrição")

def matricula_aluno(dados_matricula: Inscricao, session: Session):
    matricula = Inscricao()

