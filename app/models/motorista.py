from sqlalchemy import ForeignKey, BigInteger, Float
from sqlalchemy.orm import Mapped, mapped_column
from app.model.usuario import UsuarioModel

class MotoristaModel(UsuarioModel):
    __tablename__ = "motorista"

    id_motorista: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    id_usuario: Mapped[int] = mapped_column(BigInteger, ForeignKey('usuario.id_usuario', ondelete="CASCADE"), unique=True, nullable=False)

    media_avaliacao: Mapped[float] = mapped_column("{:.1f}".format(Float))
    cnh: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
