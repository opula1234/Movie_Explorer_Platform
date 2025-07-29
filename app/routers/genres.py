from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from app.database.db_connection import get_db
from app.schemas.genre_model import GenreModel, GenreResponse
from rich import panel, print
from app.logger.logger import logger
router = APIRouter()


@router.post("/", response_model=List[GenreResponse])
async def create_genre(genre: GenreModel, db=Depends(get_db)):
    genre_data = genre.model_dump()
    check_data = [doc async for doc in db.genres.find()]
    check = [x for x in check_data if x.get("name") == genre_data.get("name")]
    if check:
        raise HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED,
                            detail=f"Genre data is already available")
    genre_data["name"] = genre_data["name"].lower()
    response = await db.genres.insert_one(genre_data)
    logger.info(
        f"Genres data has been updated in DB {str(response.inserted_id)}")
    genre_data = [doc async for doc in db.genres.find({"_id": response.inserted_id})]
    if not genre_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Details Not Found..."
        )
    print(panel.Panel(
        f"Added {genre_data} details to DB...", border_style="green"))
    return genre_data


@router.get("/", response_model=List[GenreResponse])
async def get_genres(db=Depends(get_db)):
    genres_data = [doc async for doc in db.genres.find()]
    if not genres_data:
        print(panel.Panel(f"Details Not Found...", border_style="red"))
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Details Not Found..."
        )
    print(panel.Panel(
        f"list of genres - {genres_data}", border_style="green"))
    return genres_data
