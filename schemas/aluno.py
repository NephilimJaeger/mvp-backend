from pydantic import BaseModel, Field
from schemas.pessoa import PessoaBase
from sqlalchemy.orm.session import Session
from models import Aluno, Matricula


class AlunoBase(BaseModel):
    """
    Define os dados necessários para cadastrar um aluno.
    
    """

    pessoa_info: PessoaBase


class AlunoPath(BaseModel):
    """
    Modelo para identicação de um aluno.

    Usado no caminho da operação da API para identificar um aluno específico por meio de seu CPF.

    """

    cpf_aluno: str = Field(..., description="CPF do aluno")


def cadastra_aluno(dados_aluno: AlunoBase, session: Session):
    """
    Cadastra um novo aluno no banco de dados.

    Recebe os dados de um aluno e uma sessão de banco de dados como parâmetros. Cria uma nova instância do modelo Aluno com as informações fornecidas, adiciona essa instância à sessão e, em seguida, realiza um commit para salvar as alterações no banco de dados.

    :param dados_aluno: Um objeto AlunoBase contendo as informações do aluno a ser cadastrado.
    :param session: Uma sessão do banco de dados SQLAlchemy para realizar operações de banco de dados.
    :return: Um dicionário contendo uma mensagem de sucesso.
    """
    aluno = Aluno(pessoa_info=dados_aluno.pessoa_info)
    session.add(aluno)
    session.commit()
    return {"mensagem": "Aluno cadastrado com sucesso"}
