from sqlalchemy import Integer, Float, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class CombustivelModel(Base):
    __tablename__ = "combustivel"

    id_combustivel: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    descricao: Mapped[str] = mapped_column(VARCHAR(45))
    fator_carbono: Mapped[float] = mapped_column("{:.2f}".format(Float), nullable=False)
