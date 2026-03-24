
from enum import Enum
from typing import Optional
from pydantic import BaseModel
# from enum import Enum
# from sqlalchemy import int, int, Enum, str

class PropriedadeEnum(str, Enum):
    proprio="proprio"
    alugado="alugado"

class ModeloSchema(BaseModel):
    id_modelo: int
    id_combustivel: int

    nome_modelo: str
    cor: str
    fabricante: str
    ano: int
    capacidade: int
    propriedade: PropriedadeEnum

    class Config:
        from_attributes = True

class ModeloUpdateSchema(BaseModel):
    id_modelo: Optional[int]
    id_combustivel: Optional[int]

    nome_modelo: Optional[str]
    cor: Optional[str]
    fabricante: Optional[str]
    ano: Optional[int]
    capacidade: Optional[int]
    propriedade: Optional[PropriedadeEnum]

    class Config:
        from_attributes = True
