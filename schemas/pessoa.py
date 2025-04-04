from pydantic import BaseModel


class PessoaBase(BaseModel):
    """
    Modelo base para representar uma pessoa.

    """

    nome: str
    cpf: str
    telefone: str
    cep: str
    numero: str
    email: str
    data_nascimento: str
