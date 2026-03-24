
from sqlalchemy import Boolean, BigInteger, Integer, CHAR, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class VeiculoModel (Base):
    __tablename__ = "veiculo"

    id_veiculo: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    id_modelo: Mapped[int] = mapped_column(Integer, ForeignKey('modelo.id_modelo', ondelete="CASCADE"), unique=True, nullable=False)
    id_classe: Mapped[int] = mapped_column(Integer, ForeignKey('classe.id_classe', ondelete="CASCADE"), unique=True, nullable=False)

    placa: Mapped[str] = mapped_column(CHAR(7), unique=True, nullable=False)
    seguro: Mapped[bool] = mapped_column(Boolean, nullable=False)
    