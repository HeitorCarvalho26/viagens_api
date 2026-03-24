
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import BigInteger, DateTime

class MotoristaVeiculoSchema(BaseModel):
    id_motorista: BigInteger
    id_veiculo: BigInteger

    datahora_disp: Optional[DateTime]
    datahora_indisp: Optional[DateTime]

    class Config:
        from_attributes = True

class MotoristaVeiculoUpdateSchema(BaseModel):
    id_motorista: Optional[BigInteger]
    id_veiculo: Optional[BigInteger]

    datahora_disp: Optional[DateTime]
    datahora_indisp: Optional[DateTime]

    class Config:
        from_attributes = True
