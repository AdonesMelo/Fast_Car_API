from fastapi import APIRouter, status

from fast_car_api.schemas import CarPublic, CarSchema

# Inicialização da API
router = APIRouter(
    prefix='/api/v1/cars',
    tags=['cars'],
)

# Rota para criar um novo carro
@router.post(path='/', response_model=CarPublic, status_code=status.HTTP_201_CREATED)
def create_car(car: CarSchema):
    return car