
# Modelo de validação de dados com Pydantic
from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from enum import Enum
# from sqlalchemy import VARCHAR, int, Integer, datetime, Enum

class StatusCorridaEnum(str, Enum):
    pendente="pendente"
    em_andamento="em andamento"
    concluida="concluida"
    cancelada="cancelada"


class CorridaSchema(BaseModel):
    id_corrida: int
    id_passageiro: int
    id_motorista: int
    id_servico: int
    id_avaliacao: int

    datahora_inicio: datetime
    datahora_fim: datetime

    local_partida: str
    local_destino: str

    valor_estimado: float

    status: StatusCorridaEnum

    class Config:
        from_attributes = True

class CorridaUpdateSchema(BaseModel):
    id_corrida: Optional[int]
    id_passageiro: Optional[int]
    id_motorista: Optional[int]
    id_servico: Optional[int]
    id_avaliacao: Optional[int]

    datahora_inicio: Optional[datetime]
    datahora_fim: Optional[datetime]

    local_partida: Optional[str]
    local_destino: Optional[str]

    valor_estimado: Optional[float]

    status: Optional[Enum]

    class Config:
        from_attributes = True
