
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import Enum, BigInteger, Integer, CHAR

class VeiculoSchema(BaseModel):
    id_veiculo: BigInteger
    id_modelo: Integer
    id_classe: Integer

    placa: CHAR
    seguro: Enum

    class Config:
        from_attributes = True

class VeiculoUpdateSchema(BaseModel):
    id_veiculo: Optional[BigInteger]
    id_modelo: Optional[Integer]
    id_classe: Optional[Integer]

    placa: Optional[CHAR]
    seguro: Optional[Enum]

    class Config:
        from_attributes = True
