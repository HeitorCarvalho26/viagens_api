
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import VARCHAR, SmallInteger

class MetodoPagamentoSchema(BaseModel):
    id_metodo_pagamento: SmallInteger

    descricao: Optional[VARCHAR]
    nome_financeira: VARCHAR

    class Config:
        from_attributes = True

class MetodoPagamentoUpdateSchema(BaseModel):
    id_metodo_pagamento: Optional[SmallInteger]

    descricao: Optional[VARCHAR]
    nome_financeira: Optional[VARCHAR]

    class Config:
        from_attributes = True
