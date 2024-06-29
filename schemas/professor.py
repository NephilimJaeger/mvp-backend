from pydantic import BaseModel
from schemas.pessoa import PessoaBase


class ProfessorBase(BaseModel):
    """
    Modelo base para representar um professor .

    Este modelo estende a representação básica de uma pessoa para incluir informações específicas relacionadas a um professor.
    """

    professor_info: PessoaBase
    informacoes_adicionais: str
