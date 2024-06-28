from pydantic import BaseModel, Field
from models import Inscricao
from sqlalchemy.orm.session import Session
from schemas import AlunoBase, cadastra_aluno
from datetime import date

class InscricaoBase(BaseModel):
    dados_aluno: AlunoBase
    id_turma: int
    data_inscricao: date = Field(date.today(), description="Data da inscrição")

def matricula_aluno(dados_matricula: Inscricao, session: Session):
    try:
        cadastro = cadastra_aluno(dados_matricula.dados_aluno, session)
        matricula = Inscricao(
            id_aluno=dados_matricula.dados_aluno.pessoa_info.cpf,
            id_turma=dados_matricula.id_turma,
        )
        session.add(matricula)
        session.commit()
        return {
            "mensagem": f"Aluno matriculado na turma {dados_matricula.id_turma} com sucesso"
        }
    except Exception as e:
        session.rollback()
        return {"erro": f"Erro ao matricular aluno: {e}"}
        
