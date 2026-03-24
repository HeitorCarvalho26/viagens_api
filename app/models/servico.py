
from sqlalchemy import ForeignKey, Integer, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

class ServicoModel(Base):
    __tablename__ = "servico"

    id_servico: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_classe: Mapped[int] = mapped_column(Integer, ForeignKey('classe.id_classe', ondelete="CASCADE"), unique=True, nullable=False)

    nome_servico: Mapped[str] = mapped_column(VARCHAR(50))
