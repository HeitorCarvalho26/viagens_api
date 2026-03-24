
# Modelo de validação de dados com Pydantic
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import VARCHAR, BigInteger, Integer, DateTime, Enum

class CorridaSchema(BaseModel):
    id_corrida: BigInteger
    id_passageiro: BigInteger
    id_motorista: BigInteger
    id_servico: Integer
    id_avaliacao: BigInteger

    datahora_inicio: DateTime
    datahora_fim: DateTime

    local_partida: VARCHAR
    local_destino: VARCHAR

    valor_estimado: float

    status: Enum

    class Config:
        from_attributes = True

class CorridaUpdateSchema(BaseModel):
    id_corrida: Optional[BigInteger]
    id_passageiro: Optional[BigInteger]
    id_motorista: Optional[BigInteger]
    id_servico: Optional[Integer]
    id_avaliacao: Optional[BigInteger]

    datahora_inicio: Optional[DateTime]
    datahora_fim: Optional[DateTime]

    local_partida: Optional[VARCHAR]
    local_destino: Optional[VARCHAR]

    valor_estimado: Optional[float]

    status: Optional[Enum]

    class Config:
        from_attributes = True
