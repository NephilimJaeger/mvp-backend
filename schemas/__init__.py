from schemas.turma import (
    TurmaDisplay,
    mostra_turmas,
    atualiza_turma,
    TurmaUpdate,
    TurmaPath,
)
from schemas.aluno import AlunoBase, AlunoPath, cadastra_aluno
from schemas.matricula import (
    MatriculaBase,
    matricula_aluno,
    cancela_matricula,
    CancelarMatriculaPath,
    MatriculaCanceladaDisplay,
)
from schemas.error import ErrorSchema
from schemas.professor import ProfessorBase
