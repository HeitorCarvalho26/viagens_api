from sqlalchemy import BigInteger, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class MotoristaVeiculoModel(Base):
    __tablename__ = "motorista_veiculo"

    id_motorista: Mapped[int] = mapped_column(BigInteger, ForeignKey('motorista.id_motorista', ondelete="CASCADE"), primary_key=True, autoincrement=True)
    id_veiculo: Mapped[int] = mapped_column(BigInteger, ForeignKey('veiculo.id_veiculo', ondelete="CASCADE"), primary_key=True, autoincrement=True)

    datahora_disp: Mapped[DateTime] = mapped_column(DateTime)
    datahora_indisp: Mapped[DateTime] = mapped_column(DateTime)