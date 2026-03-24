
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.passageiro import PassageiroModel
from app.schema.passageiro import PassageiroSchema, PassageiroUpdateSchema

passageiro = APIRouter()

@passageiro.post("/")
async def criar_passageiro(dados: PassageiroSchema, db: Session = Depends(get_db)):
    novo_passageiro = PassageiroModel(**dados.model_dump())
    db.add(novo_passageiro)
    db.commit()
    db.refresh(novo_passageiro)
    return novo_passageiro

@passageiro.get("/passageiros")
async def listar_passageiros(db: Session = Depends(get_db)):
    return db.query(PassageiroModel).all()

@passageiro.delete("/passageiros/{id}/delete")
async def deletar_passageiro(id: int, db: Session = Depends(get_db)):
    passageiro = db.query(PassageiroModel).filter(PassageiroModel.id == id).first()

    if not passageiro:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Passageiro com ID {id} não encontrado."
        )
    
    db.delete(passageiro)
    db.commit()
    return {
        "resposta": f"Passageiro com ID {id} apagado com sucesso.",
        "passageiros": db.query(PassageiroModel).all()
    }

@passageiro.put("/passageiros/{id}/update")
async def atualizar_passageiro(id: int, dados: PassageiroUpdateSchema, db: Session = Depends(get_db)):
    passageiro = db.query(PassageiroModel).filter(PassageiroModel.id == id).first()

    if not passageiro:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Passageiro com ID {id} não encontrado."
        )
    
    for campo, valor in dados.model_dump().items():
        setattr (passageiro, campo, valor)

    db.commit()
    db.refresh(passageiro)
    
    return passageiro
