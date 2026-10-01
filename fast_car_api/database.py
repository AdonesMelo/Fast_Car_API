from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base de dados
DATABASE_URL = 'sqlite:///cars.db'

# Conexão com o banco de dados
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Função para criar uma sessão do banco de dados
def get_session():
    '''
    Retorna uma sessão do banco de dados
    '''
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()