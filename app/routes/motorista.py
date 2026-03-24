
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.motorista import MotoristaModel
from app.schema.motorista import MotoristaSchema, MotoristaUpdateSchema

motorista = APIRouter()

@motorista.post("/")
async def criar_motorista(dados: MotoristaSchema, db: Session = Depends(get_db)):
    novo_motorista = MotoristaModel(**dados.model_dump())
    db.add(novo_motorista)
    db.commit()
    db.refresh(novo_motorista)
    return novo_motorista

@motorista.get("/motoristas")
async def listar_motoristas(db: Session = Depends(get_db)):
    return db.query(MotoristaModel).all()

@motorista.delete("/motoristas/{id}/delete")
async def deletar_motorista(id: int, db: Session = Depends(get_db)):
    motorista = db.query(MotoristaModel).filter(MotoristaModel.id == id).first()

    if not motorista:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Motorista com ID {id} não encontrado."
        )
    
    db.delete(motorista)
    db.commit()
    return {
        "resposta": f"Motorista com ID {id} apagado com sucesso", 
        "motoristas": db.query(MotoristaModel).all()
    }

@motorista.put("/motoristas/{id}/update")
async def atualizar_motorista(id: int, dados: MotoristaUpdateSchema, db: Session = Depends(get_db)):
    motorista = db.query(MotoristaModel).filter(MotoristaModel.id == id).first()

    if not motorista:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Motorista com ID {id} não encontrado."
        )
    
    for campo, valor in dados.model_dump().items():
        setattr (motorista, campo, valor)

    db.commit()
    db.refresh(motorista)

    return motorista
