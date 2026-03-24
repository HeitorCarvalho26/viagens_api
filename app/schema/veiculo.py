
# from enum import Enum
from typing import Optional
from pydantic import BaseModel
# from sqlalchemy import Enum, BigInteger, Integer, CHAR


class VeiculoSchema(BaseModel):
    id_veiculo: int
    id_modelo: int
    id_classe: int

    placa: str
    seguro: bool

    class Config:
        from_attributes = True

class VeiculoUpdateSchema(BaseModel):
    id_veiculo: Optional[int]
    id_modelo: Optional[int]
    id_classe: Optional[int]

    placa: Optional[str]
    seguro: Optional[bool]

    class Config:
        from_attributes = True
