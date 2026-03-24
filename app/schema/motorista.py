
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import BigInteger, Float

class MotoristaSchema(BaseModel):
    id_motorista: BigInteger
    id_usuario: BigInteger

    media_avaliacao: Optional[Float]
    cnh: BigInteger

    class Config:
        from_attributes = True

class MotoristaUpdateSchema(BaseModel):
    id_motorista: Optional[BigInteger]
    id_usuario: Optional[BigInteger]

    media_avaliacao: Optional[Float]
    cnh: Optional[BigInteger]

    class Config:
        from_attributes = True
