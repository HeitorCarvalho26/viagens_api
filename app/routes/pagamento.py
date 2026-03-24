from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.pagamento import PagamentoModel
from app.schema.pagamento import PagamentoSchema, PagamentoUpdateSchema

pagamento = APIRouter()

@pagamento.post("/")
async def criar_pagamento(dados: PagamentoSchema, db: Session = Depends(get_db)):
    novo_pagamento = PagamentoModel(**dados.model_dump())
    db.add(novo_pagamento)
    db.commit()
    db.refresh(novo_pagamento)
    return novo_pagamento

@pagamento.get("/pagamentos")
async def listar_pagamentos(db: Session = Depends(get_db)):
    return db.query(PagamentoModel).all()

@pagamento.delete("/pagamentos/{id}/delete")
async def deletar_pagamento(id: int, db: Session = Depends(get_db)):
    pagamento = db.query(PagamentoModel).filter(PagamentoModel.id == id).first()

    if not pagamento:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Pagamento com ID {id} não encontrado."
        )
    
    db.delete(pagamento)
    db.commit()
    return {
        "resposta": f"Pagamento com ID {id} apagado com sucesso.",
        "pagamentos": db.query(PagamentoModel).all()
    }

@pagamento.put("/pagamento/{id}/update")
async def atualizar_pagamento(id: int, dados: PagamentoUpdateSchema, db: Session = Depends(get_db)):
    pagamento = db.query(PagamentoModel).filter(PagamentoModel.id == id).first()

    if not pagamento:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Pagamento com ID {id} não encontrado."
        )
    
    for campo, valor in dados.model_dump().items():
        setattr (pagamento, campo, valor)

    db.commit()
    db.refresh(pagamento)

    return pagamento