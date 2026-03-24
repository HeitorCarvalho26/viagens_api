
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.servico import ServicoModel
from app.schema.servico import ServicoSchema, ServicoUpdateSchema

servico = APIRouter()

@servico.post("/")
async def criar_servico(dados: ServicoSchema, db: Session = Depends(get_db)):
    novo_servico = ServicoModel(**dados.model_dump())
    db.add(novo_servico)
    db.commit()
    db.refresh(novo_servico)
    return novo_servico

@servico.get("/servicos")
async def listar_servicos(db: Session = Depends(get_db)):
    return db.query(ServicoModel).all()

@servico.delete("/servicos/{id}/delete")
async def deletar_servico(id: int, db: Session = Depends(get_db)):
    servico = db.query(ServicoModel).filter(ServicoModel.id == id).first()

    if not servico:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Serviço com ID {id} não encontrado."
        )
    
    db.delete(servico)
    db.commit()
    return {
        "resposta": f"Serviço com ID {id} apagado com sucesso.",
        "servicos": db.query(ServicoModel).all()
    }

@servico.put("/servico/{id}/update")
async def atualizar_servico(id: int, dados: ServicoUpdateSchema, db: Session = Depends(get_db)):
    servico = db.query(ServicoModel).filter(ServicoModel.id == id).first()

    if not servico:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Serviço com ID {id} não encontrado."
        )
    
    for campo, valor in dados.model_dump().items():
        setattr (servico, campo, valor)

    db.commit()
    db.refresh(servico)
    return servico
