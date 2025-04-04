from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
from flask import redirect
from models import Turma, Matricula, busca_endereco
from database import session
from schemas import *

info = Info(title="API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

home_tag = Tag(
    name="Documentação",
    description="Seleção de documentação: Swagger, Redoc ou RapiDoc",
)
aluno_tag = Tag(name="Alunos", description="Cadastro e visualização de alunos")
turma_tag = Tag(name="Turmas", description="Visualização das turmas disponíveis")
endereco_tag = Tag(name="Endereços", description="Consulta de endereço via CEP")


@app.get("/", tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação."""
    return redirect("/openapi")


@app.get(
    "/turmas",
    tags=[turma_tag],
    responses={"200": TurmaDisplay, "400": ErrorSchema},
)
def get_turmas():
    """
    Consulta o banco de dados para obter todas as turmas cadastradas e as retorna ao usuário

    Obtém a lista de todas as turmas disponíveis.

    :return: Lista de turmas disponíveis ou mensagem de erro em caso de falha na consulta.
    """
    try:
        turmas = session.query(Turma).all()
        return mostra_turmas(turmas, session), 200
    except Exception as e:
        return {"erro": f"Erro ao consultar turmas: {e}"}, 400


@app.get(
    "/alunos/<cpf_aluno>/turmas",
    tags=[aluno_tag],
    responses={"200": TurmaDisplay, "404": ErrorSchema},
)
def get_turmas_por_cpf(path: AlunoPath):
    """
    Endpoint para buscar turmas associadas ao CPF do aluno.

    :param cpf_aluno: CPF do aluno como string.
    :return: Lista de turmas associadas ao aluno ou mensagem de erro se não encontrado.
    """
    id_turmas = (
        session.query(Matricula.id_turma)
        .filter(Matricula.id_aluno == path.cpf_aluno)
        .all()
    )
    id_turmas_values = [id_turma[0] for id_turma in id_turmas]
    turmas = session.query(Turma).filter(Turma.id_turma.in_(id_turmas_values)).all()
    if turmas:
        return mostra_turmas(turmas, session)
    else:
        return {"erro": "Aluno não encontrado ou não matriculado em nenhuma turma"}, 404


@app.post(
    "/matricula",
    tags=[aluno_tag],
    responses={"200": MatriculaBase, "400": ErrorSchema},
)
def matricular_aluno(form: MatriculaBase):
    """
    Endpoint para matricular um aluno em uma turma.

    Recebe os dados para realizar o cadastro do aluno no sistema e realiza a matrícula do aluno na turma especificada.

    :param form: Objeto MatriculaBase contendo os dados necessários para a matrícula do aluno.
    :return: Dados da matrícula realizada ou mensagem de erro em caso de falha na matrícula.
    """
    try:
        matricula = matricula_aluno(form, session)
        return matricula, 200
    except Exception as e:
        session.rollback()
        return {"erro": f"Erro ao matricular aluno: {e}"}, 400


@app.get(
    "/endereco",
    tags=[endereco_tag],
    responses={"200": EnderecoResponse, "400": ErrorSchema},
)
def get_endereco(query: EnderecoQuery):
    """
    Endpoint para buscar endereço a partir do CEP.
    Utiliza a API ViaCEP para obter os dados do endereço.

    :param query: Objeto contendo o CEP a ser consultado.
    :return: Dados do endereço ou mensagem de erro.
    """
    try:
        endereco = busca_endereco(query.cep)
        if not endereco:
            return {"erro": "CEP não encontrado ou invalido"}, 404
        return endereco, 200
    except Exception as e:
        return {"erro": f"Erro ao buscar endereço: {e}"}, 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
