
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.classe import ClasseModel
from app.schema.classe import ClasseSchema, ClasseUpdateSchema

classe = APIRouter()

@classe.post("/")
async def criar_classe(dados: ClasseSchema, db: Session = Depends(get_db)):
    nova_classe = ClasseModel(**dados.model_dump())
    db.add(nova_classe)
    db.commit()
    db.refresh(nova_classe)
    return nova_classe

@classe.get("/classes")
async def listar_classes(db: Session = Depends(get_db)):
    return db.query(ClasseModel).all()

@classe.delete("/classe/{id}/delete")
async def deletar_classe(id: int, db: Session = Depends(get_db)):
    classe = db.query(ClasseModel).filter(ClasseModel.id == id).first()

    if not classe:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Classe com ID {id} não encontrada."
        )
    
    db.delete(classe)
    db.commit()
    return {
        "resposta": f"Classe com ID {id} apagada com sucesso.",
        "classes": db.query(ClasseModel).all()
    }

@classe.put("/classes/{id}/update")
async def atualizar_classe(id: int, dados: ClasseUpdateSchema, db: Session = Depends(get_db)):
    classe = db.query(ClasseModel).filter(ClasseModel.id == id).first()

    if not classe:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Classe com ID {id} não encontrada."
        )
    
    for campo, valor in dados.model_dump().items():
        setattr (classe, campo, valor)

    db.commit()
    db.refresh(classe)

    return classe
