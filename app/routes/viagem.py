from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.viagem import ViagemModel
from app.schema.viagem import ViagemSchema, ViagemUpdateSchema

viagem = APIRouter()

@viagem.post("/")
async def criar_viagem(dados: ViagemSchema, db: Session = Depends(get_db)):
    nova_viagem = ViagemModel(**dados.model_dump())
    db.add(nova_viagem)
    db.commit()
    db.refresh(nova_viagem)
    return nova_viagem

@viagem.get("/viagens")
async def listar_viagens(db: Session = Depends(get_db)):
    return db.query(ViagemModel).all()

@viagem.delete("/viagens/{id}/delete")
async def deletar_viagem(id: int, db: Session = Depends(get_db)):
    viagem = db.query(ViagemModel).filter(ViagemModel.id == id).first()

    if not viagem:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Viagem com ID {id} não encontrada."
        )
    
    db.delete(viagem)
    db.commit()
    return {
        "resultado": "Viagem com ID {id} apagada com sucesso.",
        "viagens": db.query(ViagemModel).all()
    }

@viagem.put("/viagens/{id}/update")
async def atualizar_viagem(id: int, dados: ViagemUpdateSchema, db: Session = Depends(get_db)):
    viagem = db.query(ViagemModel).filter(ViagemModel.id == id).first()

    if not viagem:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Viagem com ID {id} não encontrada."
        )
    
    for campo, valor in dados.model_dump().items():
        setattr (viagem, campo, valor)

    db.commit()
    db.refresh(viagem)
    
    return viagem