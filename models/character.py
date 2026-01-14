from pydantic import BaseModel, HttpUrl, Field
from typing import List, Optional

# 1. Character model
class Character(BaseModel):
    # Use Field to ensure ID is always positive
    id: int = Field(gt=0)
    name: str
    status: str
    species: str
    gender: str
    image: HttpUrl
    


# 2. Location model
class Location(BaseModel):
    id: int
    name: str
    type: str
    dimension: str

# 3. Episode model
class Episode(BaseModel):
    id: int
    name: str
    air_date: str
    episode: str  # Example: "S01E01"