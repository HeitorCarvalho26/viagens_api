
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.motorista_veiculo import MotoristaVeiculoModel
from app.schema.motorista_veiculo import MotoristaVeiculoSchema, MotoristaVeiculoUpdateSchema

motorista_veiculo = APIRouter()

@motorista_veiculo.post("/")
async def criar_motorista_veiculo(dados: MotoristaVeiculoSchema, db: Session = Depends(get_db)):
    novo_motorista_veiculo = MotoristaVeiculoModel(**dados.model_dump())
    db.add(novo_motorista_veiculo)
    db.commit()
    db.refresh(novo_motorista_veiculo)
    return novo_motorista_veiculo

@motorista_veiculo.get("/motoristas_veiculo")
async def listar_motoristas_veiculo(db: Session = Depends(get_db)):
    return db.query(MotoristaVeiculoModel).filter(MotoristaVeiculoModel.id == id).first()

@motorista_veiculo.delete("/motoristas_veiculo/{id}/delete")
async def deletar_motorista_veiculo(id: int, db: Session = Depends(get_db)):
    motorista_veiculo = db.query(MotoristaVeiculoModel).filter(MotoristaVeiculoModel.id == id).first()

    if not motorista_veiculo:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Motorista-Veículo com ID {id} não encontrado."
        )
    
    db.delete(motorista_veiculo)
    db.commit()
    return {
        "resposta": f"Motorista-Veículo com ID {id} apagado com sucesso.",
        "motoristas-veiculo": db.query(MotoristaVeiculoModel).all()
    }

@motorista_veiculo.put("/motoristas_veiculo/{id}/update")
async def atualizar_motorista_veiculo(id: int, dados: MotoristaVeiculoUpdateSchema, db: Session = Depends(get_db)):
    motorista_veiculo = db.query(MotoristaVeiculoModel).filter(MotoristaVeiculoModel.id == id).first()

    if not motorista_veiculo:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Motorista-Veículo com ID {id} não encontrado."
        )
    
    for campo, valor in dados.model_dump().items():
        setattr (motorista_veiculo, campo, valor)

    db.commit()
    db.refresh(motorista_veiculo)

    return motorista_veiculo
