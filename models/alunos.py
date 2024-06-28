from sqlalchemy import Column
from models.pessoa import Pessoa, PessoaInfo
from datetime import date


class Aluno(Pessoa):
    __tablename__ = "alunos"

    def __init__(
        self,
        pessoa_info: PessoaInfo,
    ):
        super().__init__(pessoa_info)

