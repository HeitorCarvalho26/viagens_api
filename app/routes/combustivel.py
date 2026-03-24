from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.combustivel import CombustivelModel
from app.schema.combustivel import CombustivelSchema, CombustivelUpdateSchema

combustivel = APIRouter()

@combustivel.post("/")
async def criar_combustivel(dados: CombustivelSchema, db: Session = Depends(get_db)):
    novo_combustivel = CombustivelModel(**dados.model_dump())
    db.add(novo_combustivel)
    db.commit()
    db.refresh(novo_combustivel)
    return novo_combustivel

@combustivel.get("/combustiveis")
async def listar_combustiveis(db: Session = Depends(get_db)):
    return db.query(CombustivelModel).all()

@combustivel.delete("/combustiveis/{id}/delete")
async def deletar_combustivel(id: int, db: Session = Depends(get_db)):
    combustivel = db.query(CombustivelModel).filter(CombustivelModel.id == id).first()

    if not combustivel:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Combustível com ID {id} não encontrado."
        )
    
    db.delete(combustivel)
    db.commit()
    return {
        "resposta": f"Combustível com ID {id} apagado com sucesso.",
        "combustiveis": db.query(CombustivelModel).all()
    }
    
@combustivel.put("/combustiveis/{id}/update")
async def atualizar_combustivel(id: int, dados: CombustivelUpdateSchema, db: Session = Depends(get_db)):
    combustivel = db.query(CombustivelModel).filter(CombustivelModel.id == id).first()

    if not combustivel:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Combustível com ID {id} não encontrado."
        )
    
    for campo, valor in dados.model_dump().items():
        setattr (combustivel, campo, valor)

    db.commit()
    db.refresh(combustivel)

    return combustivel