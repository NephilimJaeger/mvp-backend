from pydantic import BaseModel, Field
from models import Matricula, Turma
from sqlalchemy.orm.session import Session
from schemas import AlunoBase, cadastra_aluno
from datetime import date


class MatriculaBase(BaseModel):
    """
    Define os dados necessários para matricular um aluno em uma turma.

    """

    dados_aluno: AlunoBase
    id_turma: int
    data_matricula: date = Field(date.today(), description="Data da inscrição")


def verifica_existencia_turma(id_turma: int, session: Session) -> bool:
    """
    Verifica se uma turma com o id_turma especificado existe no banco de dados.

    Parâmetros:
    - id_turma: int - O identificador da turma a ser verificado.
    - session: Session - A sessão do SQLAlchemy para executar a consulta ao banco de dados.

    Retorna:
    - bool: True se a turma existir, False caso contrário.
    """
    turma_existente = session.query(Turma).filter(Turma.id_turma == id_turma).first()

    return turma_existente is not None


def matricula_aluno(dados_matricula: Matricula, session: Session):
    """
    Realiza a matrícula de um aluno em uma turma, verificando primeiro se a turma existe.

    Parâmetros:
    - dados_matricula (Matricula): Objeto contendo os dados da matrícula, incluindo o aluno e a turma.
    - session (Session): Sessão do SQLAlchemy para realizar operações no banco de dados.

    Retorna:
    - dict: Mensagem de sucesso com o ID da turma em que o aluno foi matriculado, ou mensagem de erro.
    """
    if not verifica_existencia_turma(dados_matricula.id_turma, session):
        raise ValueError(f"Turma {dados_matricula.id_turma} não existe")
    cadastra_aluno(dados_matricula.dados_aluno, session)
    matricula = Matricula(
        id_aluno=dados_matricula.dados_aluno.pessoa_info.cpf,
        id_turma=dados_matricula.id_turma,
    )
    session.add(matricula)
    session.commit()
    return {
        "mensagem": f"Aluno {dados_matricula.dados_aluno.pessoa_info.nome} matriculado na turma {dados_matricula.id_turma} com sucesso",
    }
