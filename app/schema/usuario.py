
# import datetime
from typing import Optional
from pydantic import BaseModel
from datetime import datetime
# from sqlalchemy import TEXT, CHAR, VARCHAR, BigInteger, SmallInteger, Date

class UsuarioSchema(BaseModel):
    id_usuario: int
    nome: str   
    cpf: str
    idade: int
    data_nascimento: datetime
    senha: str
    email: str
    usuario: str

    class Config:
        from_attributes = True

class UsuarioUpdateSchema(BaseModel):
    id_usuario: Optional[int]
    nome: Optional[str]
    cpf: Optional[str]
    idade: Optional[int]
    data_nascimento: Optional[datetime]
    senha: Optional[str]
    email: Optional[str]
    usuario: Optional[str]

    class Config:
        from_attributes = True
