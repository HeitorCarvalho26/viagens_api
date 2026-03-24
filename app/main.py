
from fastapi import FastAPI
from app.database import Base, engine
from app.route.avaliacao import avaliacao
from app.route.classe import classe
from app.route.combustivel import combustivel
from app.route.corrida import corrida
from app.route.metodo_pagamento import metodo_pagamento
from app.route.modelo import modelo
from app.route.motorista_veiculo import motorista_veiculo
from app.route.motorista import motorista
from app.route.pagamento import pagamento
from app.route.passageiro import passageiro
from app.route.servico import servico
from app.route.usuario import usuario
from app.route.veiculo import veiculo

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
    