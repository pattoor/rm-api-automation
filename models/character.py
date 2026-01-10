from pydantic import BaseModel, HttpUrl, Field
from typing import List, Optional

# 1. Modelo de Personaje (Character)
class Character(BaseModel):
    id: int
    name: str
    status: str
    species: str
    gender: str
    image: HttpUrl
    # Usamos Field para asegurar que el ID siempre sea positivo
    id: int = Field(gt=0)


# 2. Modelo de Ubicación (Location)
class Location(BaseModel):
    id: int
    name: str
    type: str
    dimension: str

# 3. Modelo de Episodio (Episode)
class Episode(BaseModel):
    id: int
    name: str
    air_date: str
    episode: str  # Ejemplo: "S01E01"