
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import BigInteger, SmallInteger, DateTime

class AvaliacaoSchema(BaseModel):
    id_avaliacao: BigInteger

    nota_passageiro: Optional[SmallInteger]
    nota_motorista: Optional[SmallInteger]
    datahora_limite: DateTime

    class Config:
        from_attributes = True

class AvaliacaoUpdateSchema(BaseModel):
    id_avaliacao: Optional[BigInteger]

    nota_passageiro: Optional[SmallInteger]
    nota_motorista: Optional[SmallInteger]
    datahora_limite: Optional[DateTime]

    class Config:
        from_attributes = True
