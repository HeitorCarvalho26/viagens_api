
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import TEXT, CHAR, VARCHAR, BigInteger, SmallInteger, Date

class UsuarioSchema(BaseModel):
    id_usuario: BigInteger
    nome: CHAR
    cpf: CHAR
    idade: SmallInteger
    data_nascimento: Date
    senha: CHAR
    email: TEXT
    usuario: VARCHAR

    class Config:
        from_attributes = True

class UsuarioUpdateSchema(BaseModel):
    id_usuario: Optional[BigInteger]
    nome: Optional[CHAR]
    cpf: Optional[CHAR]
    idade: Optional[SmallInteger]
    data_nascimento: Optional[Date]
    senha: Optional[CHAR]
    email: Optional[TEXT]
    usuario: Optional[VARCHAR]

    class Config:
        from_attributes = True
