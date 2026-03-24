
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import Float, Integer, VARCHAR

class ClasseSchema (BaseModel):
    id_classe: Integer

    nome_classe: VARCHAR
    fator_preco: Float
    
    class Config:
        from_attributes = True

class ClasseUpdateSchema (BaseModel):
    id_classe: Optional[Integer]

    nome_classe: Optional[VARCHAR]
    fator_preco: Optional[Float]

    class Config:
        from_attributes = True
