from pydantic import BaseModel, Field
from models import busca_endereco


class EnderecoQuery(BaseModel):
    """Define parâmetros para busca de endereço por CEP."""

    cep: str = Field(
        ...,
        description="CEP do endereço para busca (somento números)",
        example="12345678",
    )


class EnderecoResponse(BaseModel):
    """Define a resposta da consulta de endereço."""

    cep: str = Field(None, description="CEP formatado")
    logradouro: str = Field(None, description="Nome da rua/avenida/etc")
    complemento: str = Field(None, description="Complemento do endereço")
    unidade: str = Field(None, description="Unidade do endereço")
    bairro: str = Field(None, description="Nome do bairro")
    localidade: str = Field(None, description="Nome da cidade")
    uf: str = Field(None, description="Sigla do estado")
    ibge: str = Field(None, description="Código IBGE do município")
    gia: str = Field(None, description="Código GIA")
    ddd: str = Field(None, description="DDD da região")
    siafi: str = Field(None, description="Código SIAFI do município")
