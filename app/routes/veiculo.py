
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.veiculo import VeiculoModel
from app.schema.veiculo import VeiculoSchema, VeiculoUpdateSchema

veiculo = APIRouter()

@veiculo.post("/")
async def criar_veiculo(dados: VeiculoSchema, db: Session = Depends(get_db)):
    novo_veiculo = VeiculoModel(**dados.model_dump())
    db.add(novo_veiculo)
    db.commit()
    db.refresh(novo_veiculo)
    return novo_veiculo

@veiculo.get("/veiculos")
async def listar_veiculos(db: Session = Depends(get_db)):
    return db.query(VeiculoModel).all()

@veiculo.delete("/veiculos/{id}/delete")
async def deletar_veiculo(id: int, db: Session = Depends(get_db)):
    veiculo = db.query(VeiculoModel).filter(VeiculoModel.id == id).first()

    if not veiculo:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Veículo com ID {id} não encontrado."
        )
    
    db.delete(veiculo)
    db.commit()
    return {
        "resposta": f"Veículo com ID {id} apagado com sucesso.",
        "veiculos": db.query(VeiculoModel).all()
    }

@veiculo.put("/veiculos/{id}/update")
async def atualizar_veiculo(id: int, dados: VeiculoUpdateSchema, db: Session = Depends(get_db)):
    veiculo = db.query(VeiculoModel).filter(VeiculoModel.id == id).first()

    if not veiculo:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Veículo com ID {id} não encontrado."
        )
    
    for campo, valor in dados.model_dump().items():
        setattr (veiculo, campo, valor)

    db.commit()
    db.refresh(veiculo)

    return veiculo
