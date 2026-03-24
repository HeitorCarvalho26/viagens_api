
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import Integer, Float, VARCHAR

class CombustivelSchema(BaseModel):
    id_combustivel: Integer

    descricao: Optional[VARCHAR]
    fator_carbono: Float

    class Config:
        from_attributes = True

class CombustivelUpdateSchema(BaseModel):
    id_combustivel: Optional[Integer]
    descricao: Optional[VARCHAR]
    fator_carbono: Optional[Float]

    class Config:
        from_attributes = True
