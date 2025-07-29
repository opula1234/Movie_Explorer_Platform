from .utils import PyObjectId
from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, Field


class GenreModel(BaseModel):
    name: str


class GenreResponse(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    name: str

    model_config = {"populate_by_name": True, "json_encoders": {ObjectId: str}}
