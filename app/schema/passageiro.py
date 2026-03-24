
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import BigInteger, Float

class PassageiroSchema(BaseModel):
    id_passageiro: BigInteger
    id_usuario: BigInteger

    media_avaliacao: Optional[Float]

    class Config:
        from_attributes = True

class PassageiroUpdateSchema(BaseModel):
    id_passageiro: Optional[BigInteger]
    id_usuario: Optional[BigInteger]

    media_avaliacao: Optional[Float]

    class Config:
        from_attributes = True
