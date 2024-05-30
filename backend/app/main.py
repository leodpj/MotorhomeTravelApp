from fastapi import FastAPI
from database import engine, Base
from routes import user_routes, camping_routes

# Criação do banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluindo as rotas
app.include_router(user_routes.router, prefix="/users", tags=["users"])
app.include_router(camping_routes.router, prefix="/campings", tags=["campings"])

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao Motorhome Travel App"}
