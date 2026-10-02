from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from fast_car_api.database import get_session
from fast_car_api.models import Car
from fast_car_api.schemas import CarPublic, CarSchema

# Inicialização da API
router = APIRouter(
    prefix='/api/v1/cars',
    tags=['cars'],
)

# Rota para criar um novo carro
@router.post(path='/', response_model=CarPublic, status_code=status.HTTP_201_CREATED)
def create_car(car: CarSchema, session: Session = Depends(get_session)):
    '''Cria um novo carro, retornando o ID do carro'''
    car = Car(**car.model_dump())
    session.add(car)
    session.commit()
    session.refresh(car)
    return car