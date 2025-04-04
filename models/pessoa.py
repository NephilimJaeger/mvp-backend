from models.base import Base
from dataclasses import dataclass
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import String, Date
from datetime import date
import requests


@dataclass
class PessoaInfo:
    nome: str
    cpf: str
    telefone: str
    cep: str
    complemento: str
    email: str
    data_nascimento: date


def busca_endereco(cep: str) -> dict:
    """
    Consulta a API ViaCEP para obter o endereço a partir do CEP.

    Args:
        cep (str): CEP a ser consultado (apenas números)

    Returns:
        dict: Dicionário com os dados do endereço ou vazio se houver erro
    """
    cep = "".join(filter(str.isdigit, cep))

    if len(cep) != 8:
        raise ValueError("CEP deve conter 8 dígitos")

    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                return data
        return {}
    except Exception:
        return {}


class Pessoa(Base):
    __abstract__ = True
    nome = Column(String)
    cpf = Column(String(11), primary_key=True)
    telefone = Column(String)
    endereco = Column(String)
    email = Column(String)
    data_nascimento = Column(Date)

    def __init__(self, pessoa_info: PessoaInfo):
        self.nome = pessoa_info.nome
        self.cpf = pessoa_info.cpf
        self.telefone = pessoa_info.telefone
        self.email = pessoa_info.email
        self.data_nascimento = pessoa_info.data_nascimento

        endereco_data = busca_endereco(pessoa_info.cep)
        if endereco_data:
            self.endereco = f"{endereco_data.get('logradouro')}, {endereco_data.get('bairro')}, {endereco_data.get('localidade')}, {endereco_data.get('uf')}"
        else:
            self.endereco = pessoa_info.complemento
