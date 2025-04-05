from models.base import Base
from dataclasses import dataclass
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import String, Date
from datetime import date

@dataclass
class PessoaInfo:
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
    data_nascimento: date


class Pessoa(Base):
    __abstract__ = True
    nome = Column(String)
    cpf = Column(String(11), primary_key=True)
    telefone = Column(String)
    endereco = Column(String)
    email = Column(String)
    data_nascimento = Column(Date)
    cep = Column(String(8))

    def __init__(self, pessoa_info: PessoaInfo):
        self.nome = pessoa_info.nome
        self.cpf = pessoa_info.cpf
        self.telefone = pessoa_info.telefone
        self.email = pessoa_info.email
        self.data_nascimento = pessoa_info.data_nascimento
        self.numero = pessoa_info.numero
        self.logradouro = pessoa_info.logradouro
        self.bairro = pessoa_info.bairro
        self.cidade = pessoa_info.cidade
        self.uf = pessoa_info.uf
        self.cep = pessoa_info.cep

        self.endereco = f"{self.logradouro},{self.numero} - {self.bairro}, {self.cidade}-{self.uf}"
