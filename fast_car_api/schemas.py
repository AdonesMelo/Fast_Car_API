from typing import Optional

from pydantic import BaseModel


class CarSchema(BaseModel):
    marca: str
    modelo: str
    cor: Optional[str] = None
    ano_fabricacao: Optional[int] = None
    ano_modelo: Optional[int] = None
    descricao: Optional[str] = None


class CarPublic(BaseModel):
    id: int
    marca: str
    modelo: str
    cor: str
    ano_fabricacao: int
    ano_modelo: int
    descricao: str