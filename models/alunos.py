from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Date
from pessoa import Pessoa, PessoaInfo
from datetime import date

class Aluno(Pessoa):
    __tablename__ = 'alunos'
    data_nascimento = Column(Date)
    data_inicio = Column(Date)

    def __repr__(self):
        return f'<Aluno {self.nome}>'
    
    def __init__(self, pessoa_info: PessoaInfo , data_nascimento: date, data_inicio: date):
        super().__init__(pessoa_info)
        self.data_nascimento = data_nascimento
        self.data_inicio = data_inicio









