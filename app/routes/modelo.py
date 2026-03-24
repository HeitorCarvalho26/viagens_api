
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.modelo import ModeloModel
from app.schema.modelo import ModeloSchema, ModeloUpdateSchema

modelo = APIRouter()

@modelo.post("/")
async def criar_modelo(dados: ModeloSchema, db: Session = Depends(get_db)):
    novo_modelo = ModeloModel(**dados.model_dump())
    db.add(novo_modelo)
    db.commit()
    db.refresh(novo_modelo)
    return novo_modelo

@modelo.get("/modelos")
async def listar_modelos(db: Session = Depends(get_db)):
    return db.query(ModeloModel).all()

@modelo.delete("/modelos/{id}/delete")
async def deletar_modelo(id: int, db: Session = Depends(get_db)):
    modelo = db.query(ModeloModel).filter(ModeloModel.id == id).first()

    if not modelo:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Modelo com ID {id} não encontrado."
        )
    
    db.delete(modelo)
    db.commit()
    return{
        "resposta": f"Modelo com ID {id} apagado com sucesso.",
        "modelos": db.query(ModeloModel).all()
    }

@modelo.put("/modelos/{id}/update")
async def atualizar_modelo(id: int, dados: ModeloUpdateSchema, db: Session = Depends(get_db)):
    modelo = db.query(ModeloModel).filter(ModeloModel.id == id).first()

    if not modelo:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Modelo com ID {id} não encontrado."
        )
    
    for campo, valor in dados.model_dump().items():
        setattr (modelo, campo, valor)

    db.commit()
    db.refresh(modelo)

    return modelo
