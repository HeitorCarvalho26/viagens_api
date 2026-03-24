
from typing import Optional
from pydantic import BaseModel
# from sqlalchemy import int, Float

class PassageiroSchema(BaseModel):
    id_passageiro: int
    id_usuario: int

    media_avaliacao: Optional[float]

    class Config:
        from_attributes = True

class PassageiroUpdateSchema(BaseModel):
    id_passageiro: Optional[int]
    id_usuario: Optional[int]

    media_avaliacao: Optional[float]

    class Config:
        from_attributes = True
