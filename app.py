from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
from flask import redirect
from models import Turma
from database import session
from schemas import *

info = Info(title="API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

home_tag = Tag(
    name="Documentação",
    description="Seleção de documentação: Swagger, Redoc ou RapiDoc",
)
turma_tag = Tag(name="Turmas", description="Visualização das turmas disponíveis")
matricula_tag = Tag(name="Matrícula", description="Matrícula de alunos")


@app.get("/", tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação."""
    return redirect("/openapi")


@app.get(
    "/turmas",
    tags=[turma_tag],
    responses={"200": TurmaDisplay, "409": ErrorSchema, "400": ErrorSchema},
)
def get_turmas():
    turmas = session.query(Turma).all()
    return mostra_turmas(turmas, session)


@app.post("/matricula", tags=[matricula_tag])
def matricular_aluno(form: Inscricao):
    cadastro = cadastra_aluno(form.dados_aluno, session)
    matricula = matricula_aluno()
    return cadastro


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
