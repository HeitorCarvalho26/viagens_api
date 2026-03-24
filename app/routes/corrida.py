
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.corrida import CorridaModel
from app.schema.corrida import CorridaSchema, CorridaUpdateSchema

corrida = APIRouter()

@corrida.post("/")
async def criar_corrida(dados: CorridaSchema, db: Session = Depends(get_db)):
    nova_corrida = CorridaModel(**dados.model_dump())
    db.add(nova_corrida)
    db.commit
    db.refresh(nova_corrida)
    return nova_corrida

@corrida.get("/corridas")
async def listar_corridas(db: Session = Depends(get_db)):
    return db.query(CorridaModel).all()

@corrida.delete("/corrida/{id}/delete")
async def deletar_corrida(id: int, db: Session = Depends(get_db)):
    corrida = db.query(CorridaModel).filter(CorridaModel.id == id).first()

    if not corrida:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Corrida com ID {id} não encontrada."
        )
    
@corrida.put("/corrida/{id}/update")
async def atualizar_corrida(id: int, dados: CorridaUpdateSchema, db: Session = Depends(get_db)):
    corrida = db.query(CorridaModel).filter(CorridaModel.id == id).first()

    if not corrida:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Corrida com ID {id} não encontrada."
        )
    
    for campo, valor, in dados.model_dump().items():
        setattr (corrida, campo, valor)

    db.commit()
    db.refresh(corrida)

    return corrida
