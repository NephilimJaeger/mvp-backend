from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import String
from models.pessoa import Pessoa, PessoaInfo


class Professor(Pessoa):
    __tablename__ = "professor"
    informacoes_adicionais = Column(String(4000))

    def __init__(self, pessoa_info: PessoaInfo, informacoes_adicionais: str):
        super().__init__(pessoa_info)
        self.informacoes_adicionais = informacoes_adicionais
