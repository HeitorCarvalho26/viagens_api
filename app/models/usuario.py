# Modelo da Tabela "Usuário" para o Banco de Dados;

from sqlalchemy import TEXT, CHAR, VARCHAR, BigInteger, SmallInteger, Date
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class UsuarioModel(Base):
    __tablename__ = "usuario"

    id_usuario: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(TEXT, nullable=False)
    cpf: Mapped[str] = mapped_column(CHAR(11), unique=True, nullable=False)
    idade: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    data_nascimento: Mapped[Date] = mapped_column(Date, nullable=False)
    senha: Mapped[str] = mapped_column(CHAR(64), nullable=False)
    email: Mapped[str] = mapped_column(TEXT, unique=True, nullable=False)
    usuario: Mapped[str] = mapped_column(VARCHAR(50), unique=True, nullable=False)