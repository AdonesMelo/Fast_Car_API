from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from fast_car_api.database import get_session
from fast_car_api.models import Car
from fast_car_api.schemas import CarList, CarPartialUpdate, CarPublic, CarSchema

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


# Rota para buscar carros
@router.get(path='/', response_model=CarList, status_code=status.HTTP_200_OK)
def list_cars(session: Session = Depends(get_session), offset: int = 0, limit: int = 100):
    '''Busca todos os carros'''
    query = session.scalars(select(Car).offset(offset).limit(limit))
    cars = query.all()
    return {'cars': cars}


# Rota para buscar um carro específico
@router.get(path='/{car_id}', response_model=CarPublic, status_code=status.HTTP_200_OK)
def get_car(car_id: int, session: Session = Depends(get_session)):
    '''Busca um carro pelo ID'''
    car = session.get(Car, car_id)
    if not car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Car not found')
    return car


# Rota para atualizar um carro
@router.put(path='/{car_id}', response_model=CarPublic, status_code=status.HTTP_201_CREATED)
def update_car(car_id: int, car: CarSchema, session: Session = Depends(get_session)):
    '''Atualiza um carro, retornando o ID do carro atualizado'''
    db_car = session.get(Car, car_id)
    if not db_car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Car not found')
    for field, value in car.model_dump().items():
        setattr(db_car, field, value)
    session.commit()
    session.refresh(db_car)
    return db_car


# Rota para atualizar um carro parcialmente
@router.patch(path='/{car_id}', response_model=CarPublic, status_code=status.HTTP_200_OK)
def patch_car(car_id: int, car: CarPartialUpdate, session: Session = Depends(get_session)):
    '''Atualiza um carro parcialmente, retornando o ID do carro atualizado'''
    db_car = session.get(Car, car_id)
    if not db_car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Car not found')
    update_data = {k: v for k,v in car.model_dump(exclude_unset=True).items()}
    for field, value in update_data.items():
        setattr(db_car, field, value)
    session.commit()
    session.refresh(db_car)
    return db_car


# Rota para excluir um carro
@router.delete(path='/{car_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_car(car_id: int, session: Session = Depends(get_session)):
    '''Exclui um carro'''
    car = session.get(Car, car_id)
    if not car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Car not found')
    session.delete(car)
    session.commit()
