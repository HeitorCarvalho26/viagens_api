from typing import Optional
from pydantic import BaseModel
from sqlalchemy import BigInteger, SmallInteger, DateTime, Float

class PagamentoSchema(BaseModel):
    id_pagamento: BigInteger
    id_corrida: BigInteger
    id_metodo_pagamento: SmallInteger

    valor: Float
    datahora_transacao: DateTime

    class Config:
        from_attributes = True

class PagamentoUpdateSchema(BaseModel):
    id_pagamento: Optional[BigInteger]
    id_corrida: Optional[BigInteger]
    id_metodo_pagamento: Optional[SmallInteger]

    valor: Optional[Float]
    datahora_transacao: Optional[DateTime]

    class Config:
        from_attributes = True