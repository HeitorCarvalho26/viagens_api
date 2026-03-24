
from typing import Optional
from pydantic import BaseModel
# from sqlalchemy import Integer, Float, VARCHAR

class CombustivelSchema(BaseModel):
    id_combustivel: int

    descricao: Optional[str]
    fator_carbono: float

    class Config:
        from_attributes = True

class CombustivelUpdateSchema(BaseModel):
    id_combustivel: Optional[int]
    descricao: Optional[str]
    fator_carbono: Optional[float]

    class Config:
        from_attributes = True
