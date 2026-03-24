from sqlalchemy import Float, Integer, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

class ClasseModel(Base):
    __tablename__ = "classe"

    id_classe: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    
    nome_classe: Mapped[str] = mapped_column(VARCHAR(45), nullable=False)
    fator_preco: Mapped[Float] = mapped_column("{:.2f}".format(Float), nullable=False)