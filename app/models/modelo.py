from sqlalchemy import ForeignKey, Integer, SmallInteger, Enum, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class ModeloModel(Base):
    __tablename__ = "modelo"

    id_modelo: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    id_combustivel: Mapped[int] = mapped_column(Integer, ForeignKey('combustivel.id_combustivel', ondelete="CASCADE"), unique=True, nullable=False)

    nome_modelo: Mapped[str] = mapped_column(VARCHAR(45), nullable=False)
    cor: Mapped[str] = mapped_column(VARCHAR(45), nullable=False)
    fabricante: Mapped[str] = mapped_column(VARCHAR(45), nullable=False)
    ano: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    capacidade: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    propriedade: Mapped[Enum] = mapped_column(Enum('Próprio', 'Alugado'), nullable=False)