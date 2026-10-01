from sqlalchemy import Column, Integer, String, Text
from fast_car_api.database import Base

class Car(Base):
    __tablename__ = 'cars' # Nome da tabela

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String, nullable=False)
    modelo = Column(String, nullable=False)
    cor = Column(String, nullable=True)
    ano_fabricacao = Column(Integer, nullable=True)
    ano_modelo = Column(Integer, nullable=True)
    descricao = Column(Text, nullable=True)
    