
from typing import Optional
from pydantic import BaseModel
from datetime import datetime
# from sqlalchemy import int, DateTime

class MotoristaVeiculoSchema(BaseModel):
    id_motorista: int
    id_veiculo: int

    datahora_disp: Optional[datetime]
    datahora_indisp: Optional[datetime]

    class Config:
        from_attributes = True

class MotoristaVeiculoUpdateSchema(BaseModel):
    id_motorista: Optional[int]
    id_veiculo: Optional[int]

    datahora_disp: Optional[datetime]
    datahora_indisp: Optional[datetime]

    class Config:
        from_attributes = True
