from pydantic import BaseModel


class PessoaBase(BaseModel):
    """
    Modelo base para representar uma pessoa.

    """

    nome: str
    cpf: str
    telefone: str
    cep: str
    logradouro: str
    numero: str
    bairro: str
    cidade: str
    uf: str
    email: str
    data_nascimento: str
