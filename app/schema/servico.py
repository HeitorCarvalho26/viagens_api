
from typing import Optional
from pydantic import BaseModel
# from sqlalchemy import Integer, VARCHAR

class ServicoSchema(BaseModel):
    id_servico: int
    id_classe: int

    nome_servico: Optional[str]

    class Config:
        from_attributes = True

class ServicoUpdateSchema(BaseModel):
    id_servico: Optional[int]
    id_classe: Optional[int]

    nome_servico: Optional[str]

    class Config:
        from_attributes = True
