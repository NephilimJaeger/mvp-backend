from pydantic import BaseModel, Field
from models import Turma, Professor
from sqlalchemy.orm.session import Session
from datetime import time
from schemas.aluno import AlunoBase


class TurmaDisplay(BaseModel):
    """
    Modelo de exibição para informações detalhadas de uma turma ao usuário.
    """

    id_turma: int = Field(..., description="Identificador da turma")
    horario: str = Field(..., description="Horário da turma")
    professor: str = Field(..., description="Nome do professor")
    nivel: str = Field(..., description="Nível da turma")
    dia_semana: str = Field(..., description="Dia da semana em que a aula ocorre")


def mostra_turmas(lista_turmas: list[Turma], session: Session):
    """
    Consulta e retorna informações detalhadas de todas as turmas listadas.

    Recebe uma lista de objetos Turma e uma sessão de banco de dados. Para cada turma na lista, consulta o banco de dados para encontrar informações sobre o professor responsável. Em seguida, compila e retorna uma lista de dicionários contendo informações detalhadas sobre cada turma.

    :param lista_turmas: Lista de objetos Turma para os quais as informações detalhadas serão retornadas.
    :param session: Sessão do banco de dados utilizada para realizar as consultas.
    :return: Dicionário contendo uma lista de turmas com suas informações detalhadas.
    """
    turmas = []
    for turma in lista_turmas:
        professor = (
            session.query(Professor).filter(Professor.cpf == turma.id_professor).first()
        )
        nome_professor = professor.nome if professor else "Sem professor cadastrado"
        turmas.append(
            {
                "id_turma": turma.id_turma,
                "horario": turma.horario.strftime("%H:%M:%S"),
                "professor": nome_professor,
                "nivel": turma.nivel,
                "dia_semana": turma.dia_semana,
            }
        )
    return {"turmas": turmas}

def atualiza_turma(id_turma: int, dados_turma: TurmaDisplay, session: Session):
    """
    Atualiza os dados de uma turma existente no banco de dados.

    :param id_turma: ID da turma a ser atualizada.
    :param dados_turma: Objeto TurmaDisplay contendo os novos dados da turma.
    :param session: Sessão do banco de dados utilizada para realizar a atualização.
    :return: Mensagem de sucesso ou erro.
    """
    turma = session.query(Turma).filter(Turma.id_turma == id_turma).first()
    if not turma:
        return {"erro": "Turma não encontrada"}, 404

    turma.horario = time.fromisoformat(dados_turma.horario)
    turma.nivel = dados_turma.nivel
    turma.dia_semana = dados_turma.dia_semana
    session.commit()
    return {"mensagem": "Turma atualizada com sucesso"}, 200
