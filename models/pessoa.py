from base import Base
from dataclasses import dataclass
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import String

@dataclass
class PessoaInfo:
    nome: str
    cpf: str
    telefone: str
    endereco: str
    email: str

class Pessoa(Base):
    __abstract__ = True
    nome = Column(String)
    cpf = Column(String(11), primary_key=True)
    telefone = Column(String)
    endereco = Column(String)
    email = Column(String)

    def __init__(self, pessoa_info: PessoaInfo):
        self.nome = pessoa_info.nome
        self.cpf = pessoa_info.cpf
        self.telefone = pessoa_info.telefone
        self.endereco = pessoa_info.endereco
        self.email = pessoa_info.email