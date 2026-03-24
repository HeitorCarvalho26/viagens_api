
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import Integer, VARCHAR

class ServicoSchema(BaseModel):
    id_servico: Integer
    id_classe: Integer

    nome_servico: Optional[VARCHAR]

    class Config:
        from_attributes = True

class ServicoUpdateSchema(BaseModel):
    id_servico: Optional[Integer]
    id_classe: Optional[Integer]

    nome_servico: Optional[VARCHAR]

    class Config:
        from_attributes = True
