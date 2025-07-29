from .utils import PyObjectId
from typing import List, Optional
from bson import ObjectId
from pydantic import BaseModel, Field


class MovieModel(BaseModel):
    title: str
    released_year: int
    genres: List[str]
    cast: List[str]
    director: str


class MovieResponse(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    title: str
    released_year: int
    genres: List[str]
    cast: List[str]
    director: str

    model_config = {"populate_by_name": True, "json_encoders": {ObjectId: str}}
