from fastapi import FastAPI

from fast_car_api.routers import router as car_router

# Inicialização da API
app = FastAPI(
    title='Fast Car API',
    description='API moderna com FastAPI',
    version='0.1.0',
)

# Inclusão das rotas da API
app.include_router(car_router)


# Rotas de acesso aos dados da API
@app.get('/')
def read_root():
    return {'status': '200 OK'}


# Roda no terminal: fastapi dev fast_car_api/app.py
