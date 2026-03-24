
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import Integer, SmallInteger, Enum, VARCHAR

class ModeloSchema(BaseModel):
    id_modelo: Integer
    id_combustivel: Integer

    nome_modelo: VARCHAR
    cor: VARCHAR
    fabricante: VARCHAR
    ano: SmallInteger
    capacidade: SmallInteger
    propriedade: Enum

    class Config:
        from_attributes = True

class ModeloUpdateSchema(BaseModel):
    id_modelo: Optional[Integer]
    id_combustivel: Optional[Integer]

    nome_modelo: Optional[VARCHAR]
    cor: Optional[VARCHAR]
    fabricante: Optional[VARCHAR]
    ano: Optional[SmallInteger]
    capacidade: Optional[SmallInteger]
    propriedade: Optional[Enum]

    class Config:
        from_attributes = True
