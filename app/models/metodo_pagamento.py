from sqlalchemy import VARCHAR, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

class MetodoPagamentoModel(Base):
    __tablename__ = "metodo_pagamento"

    id_metodo_pagamento: Mapped[int] = mapped_column(SmallInteger, primary_key=True, autoincrement=True)

    descricao: Mapped[str] = mapped_column(VARCHAR(45))
    nome_financeira: Mapped[str] = mapped_column(VARCHAR(45), nullable=False)