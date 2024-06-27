from pydantic import BaseModel
from schemas.pessoa import PessoaBase
from sqlalchemy.orm.session import Session
from models import Aluno
from datetime import date


class AlunoBase(BaseModel):
    pessoa_info: PessoaBase
    data_nascimento: date

def cadastra_aluno(dados_aluno: AlunoBase, session: Session):
    aluno = Aluno(
        pessoa_info=dados_aluno.pessoa_info, data_nascimento=dados_aluno.data_nascimento
    )
    session.add(aluno)
    session.commit()
    return {"mensagem": "Aluno cadastrado com sucesso"}
