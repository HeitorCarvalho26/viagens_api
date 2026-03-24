from sqlalchemy import Integer, BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class ViagemModel(Base):
    __tablename__ = "viagem"

    id_viagem: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    id_avaliacao: Mapped[int] = mapped_column(BigInteger, ForeignKey('avaliacao.id_avaliacao', ondelete="CASCADE"), unique=True, nullable=False)
    id_corrida: Mapped[int] = mapped_column(BigInteger, ForeignKey('corrida.id_corrida', ondelete="CASCADE"), unique=True, nullable=False)
    id_modelo: Mapped[int] = mapped_column(Integer, ForeignKey('modelo.id_modelo', ondelete="CASCADE"), unique=True, nullable=False)
    id_motorista: Mapped[int] = mapped_column(BigInteger, ForeignKey('motorista.id_motorista', ondelete="CASCADE"), unique=True, nullable=False)
    id_pagamento: Mapped[int] = mapped_column(BigInteger, ForeignKey('pagamento.id_pagamento', ondelete="CASCADE"), unique=True, nullable=False)
    id_passageiro: Mapped[int] = mapped_column(BigInteger, ForeignKey('passageiro.id_passageiro', ondelete="CASCADE"), unique=True, nullable=False)
    id_servico: Mapped[int] = mapped_column(Integer, ForeignKey('servico.id_servico', ondelete="CASCADE"), unique=True, nullable=False)
    id_veiculo: Mapped[int] = mapped_column(BigInteger, ForeignKey('veiculo.id_veiculo', ondelete="CASCADE"), unique=True, nullable=False)