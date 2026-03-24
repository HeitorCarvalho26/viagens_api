from typing import Optional
from pydantic import BaseModel
from datetime import datetime
# from sqlalchemy import BigInteger, SmallInteger, DateTime, Float

class PagamentoSchema(BaseModel):
    id_pagamento: int
    id_corrida: int
    id_metodo_pagamento: int

    valor: float
    datahora_transacao: datetime

    class Config:
        from_attributes = True

class PagamentoUpdateSchema(BaseModel):
    id_pagamento: Optional[int]
    id_corrida: Optional[int]
    id_metodo_pagamento: Optional[int]

    valor: Optional[float]
    datahora_transacao: Optional[datetime]

    class Config:
        from_attributes = True