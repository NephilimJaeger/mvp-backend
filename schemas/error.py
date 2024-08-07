from pydantic import BaseModel


class ErrorSchema(BaseModel):
    """Define como uma mensagem de erro deve ser retornada."""

    mensagem: str
