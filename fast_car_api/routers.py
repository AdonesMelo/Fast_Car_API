from fastapi import APIRouter

# Inicialização da API
router = APIRouter(
    prefix='/api/v1/cars',
    tags=['cars'],
)


# Rotas de acesso aos dados da API
@router.get('/')
def list_cars():
    return {
        'cars': [
            {'id': 1, 'modelo': 'Golf GTI'},
            {'id': 2, 'modelo': 'Audi A3'},
            {'id': 3, 'modelo': 'Mustang GT'},
        ]
    }
