from sqlalchemy import BigInteger, SmallInteger, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

class AvaliacaoModel(Base):
    __tablename__ = "avaliacao"

    id_avaliacao: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)

    nota_passageiro: Mapped[int] = mapped_column(SmallInteger)
    nota_motorista: Mapped[int] = mapped_column(SmallInteger)
    datahora_limite: Mapped[DateTime] = mapped_column(DateTime, nullable=False)