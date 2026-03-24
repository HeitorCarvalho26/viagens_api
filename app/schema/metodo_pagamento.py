
from typing import Optional
from pydantic import BaseModel
# from sqlalchemy import str, int

class MetodoPagamentoSchema(BaseModel):
    id_metodo_pagamento: int

    descricao: Optional[str]
    nome_financeira: str

    class Config:
        from_attributes = True

class MetodoPagamentoUpdateSchema(BaseModel):
    id_metodo_pagamento: Optional[int]

    descricao: Optional[str]
    nome_financeira: Optional[str]

    class Config:
        from_attributes = True
