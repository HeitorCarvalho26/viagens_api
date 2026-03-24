from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.usuario import UsuarioModel
from app.schema.usuario import UsuarioSchema, UsuarioUpdateSchema

usuario = APIRouter()

@usuario.post("/")
async def criar_usuario(dados: UsuarioSchema, db: Session = Depends(get_db)):
    novo_usuario = UsuarioModel(**dados.model_dump())
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

@usuario.get("/usuarios")
async def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(UsuarioModel).all()

@usuario.delete("/usuarios/{id}/delete")
async def deletar_usuario(id: int, db: Session = Depends(get_db)):
    usuario = db.query(UsuarioModel).filter(UsuarioModel.id == id).first()

    if not usuario:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Usuário com ID {id} não encontrado."
        )
    
    db.delete(usuario)
    db.commit()
    return {
        "resultado": f"Usuário com ID {id} apagado com sucesso.",
        "usuarios": db.query(UsuarioModel).all()
    }

@usuario.put("/usuarios/{id}/update")
async def atualizar_usuario(id: int, dados: UsuarioUpdateSchema, db: Session = Depends(get_db)):
    usuario = db.query(UsuarioModel).filter(UsuarioModel.id == id).filter()

    if not usuario:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Usuário com ID {id} não encontrado."
        )
    
    for campo, valor in dados.model_dump().items():
        setattr (usuario, campo, valor)

    db.commit()
    db.refresh(usuario)
    return usuario