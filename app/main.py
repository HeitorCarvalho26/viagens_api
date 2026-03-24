
from fastapi import FastAPI
from app.database import Base, engine
from app.routes.avaliacao import avaliacao
from app.routes.classe import classe
from app.routes.combustivel import combustivel
from app.routes.corrida import corrida
from app.routes.metodo_pagamento import metodo_pagamento
from app.routes.modelo import modelo
from app.routes.motorista_veiculo import motorista_veiculo
from app.routes.motorista import motorista
from app.routes.pagamento import pagamento
from app.routes.passageiro import passageiro
from app.routes.servico import servico
from app.routes.usuario import usuario
from app.routes.veiculo import veiculo

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(avaliacao)
app.include_router(classe)
app.include_router(combustivel)
app.include_router(corrida)
app.include_router(metodo_pagamento)
app.include_router(modelo)
app.include_router(motorista_veiculo)
app.include_router(motorista)
app.include_router(pagamento)
app.include_router(passageiro)
app.include_router(servico)
app.include_router(usuario)
app.include_router(veiculo)

@app.get("/")
async def health_check():
    return {"status": "API Online"}
    