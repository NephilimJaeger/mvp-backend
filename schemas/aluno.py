from pydantic import BaseModel, Field
from schemas.pessoa import PessoaBase
from sqlalchemy.orm.session import Session
from models import Aluno
from datetime import date

class AlunoBase(BaseModel):
    pessoa_info: PessoaBase

def cadastra_aluno(dados_aluno: AlunoBase, session: Session):
    aluno = Aluno(
        pessoa_info=dados_aluno.pessoa_info 
    )
    session.add(aluno)
    session.commit()
    return {"mensagem": "Aluno cadastrado com sucesso"}
