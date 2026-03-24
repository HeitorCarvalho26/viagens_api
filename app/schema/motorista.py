
from typing import Optional
from pydantic import BaseModel
# from sqlalchemy import int, Float

class MotoristaSchema(BaseModel):
    id_motorista: int
    id_usuario: int

    media_avaliacao: Optional[float]
    cnh: int

    class Config:
        from_attributes = True

class MotoristaUpdateSchema(BaseModel):
    id_motorista: Optional[int]
    id_usuario: Optional[int]

    media_avaliacao: Optional[float]
    cnh: Optional[int]

    class Config:
        from_attributes = True
