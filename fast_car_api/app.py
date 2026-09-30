from fastapi import FastAPI

# Inicialização da API
app = FastAPI(
    title="Fast Car API",
    description="API moderna com FastAPI",
    version="0.1.0",
)

# Rotas de acesso aos dados da API
@app.get("/")
def read_root():
    return {"status": "ok 200"}

# Roda no terminal: fastapi dev fast_car_api/app.py