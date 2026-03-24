
from sqlalchemy import BigInteger, Integer
from pydantic import BaseModel
from typing import Optional

class ViagemSchema(BaseModel):
    id_viagem: BigInteger
    id_avaliacao: BigInteger
    id_corrida: BigInteger
    id_modelo: Integer
    id_motorista: BigInteger
    id_pagamento: BigInteger
    id_passageiro: BigInteger
    id_servico: Integer
    id_veiculo: BigInteger

    class Config:
        from_attributes = True

class ViagemUpdateSchema(BaseModel):
    id_viagem: Optional[BigInteger]
    id_avaliacao: Optional[BigInteger]
    id_corrida: Optional[BigInteger]
    id_modelo: Optional[Integer]
    id_motorista: Optional[BigInteger]
    id_pagamento: Optional[BigInteger]
    id_passageiro: Optional[BigInteger]
    id_servico: Optional[Integer]
    id_veiculo: Optional[BigInteger]
