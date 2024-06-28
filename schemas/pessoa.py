from pydantic import BaseModel


class PessoaBase(BaseModel):
    nome: str
    cpf: str
    telefone: str
    endereco: str
    email: str
    data_nascimento: str
