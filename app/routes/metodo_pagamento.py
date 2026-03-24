
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.metodo_pagamento import MetodoPagamentoModel
from app.schema.metodo_pagamento import MetodoPagamentoSchema, MetodoPagamentoUpdateSchema

metodo_pagamento = APIRouter()

@metodo_pagamento.post("/")
async def criar_metodo_pagamento(dados: MetodoPagamentoSchema, db: Session = Depends(get_db)):
    novo_metodo_pagamento = MetodoPagamentoModel(**dados.model_dump())
    db.add(novo_metodo_pagamento)
    db.commit()
    db.refresh(novo_metodo_pagamento)
    return novo_metodo_pagamento

@metodo_pagamento.get("/metodos_pagamento")
async def listar_metodos_pagamento(db: Session = Depends(get_db)):
    return db.query(MetodoPagamentoModel).all()

@metodo_pagamento.delete("/metodos_pagamento/{id}/delete")
async def deletar_metodo_pagamento(id: int, db: Session = Depends(get_db)):
    metodo_pagamento = db.query(MetodoPagamentoModel).filter(MetodoPagamentoModel.id == id).first()

    if not metodo_pagamento:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Metodo de Pagamento com ID {id} não encontrado."
        )
    
    db.delete(metodo_pagamento)
    db.commit()
    return {
        "resposta": f"Método de Pagamento com ID {id} apagado com sucesso.",
        "metodos_pagamento": db.query(MetodoPagamentoModel).all()
    }

@metodo_pagamento.put("/metodos_pagamento/{id}/update")
async def atualizar_metodo_pagamento(id: int, dados: MetodoPagamentoUpdateSchema, db: Session = Depends(get_db)):
    metodo_pagamento = db.query(MetodoPagamentoModel).filter(MetodoPagamentoModel.id == id).first()

    if not metodo_pagamento:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Metodo de Pagamento com ID {id} não encontrado."
        )
    
    for campo, valor in dados.model_dump().items():
        setattr (metodo_pagamento, campo, valor)

    db.commit()
    db.refresh(metodo_pagamento)

    return metodo_pagamento
