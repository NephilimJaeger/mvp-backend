from schemas.turma import TurmaDisplay, mostra_turmas, atualiza_turma
from schemas.aluno import AlunoBase, AlunoPath, cadastra_aluno
from schemas.matricula import (
    MatriculaBase,
    matricula_aluno,
    cancela_matricula,
    MatriculaPath,
)
from schemas.error import ErrorSchema
from schemas.professor import ProfessorBase
