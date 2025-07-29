from fastapi import APIRouter, HTTPException, status, Depends
from app.database.db_connection import get_db
from app.schemas.movies_model import MovieModel, MovieResponse
from typing import List
from rich import panel, print
from app.logger.logger import logger
router = APIRouter()


@router.post("/", response_model=list[MovieResponse])
async def create_movie(movie: MovieModel, db=Depends(get_db)):
    movie_data = movie.model_dump()
    check_data = [doc async for doc in db.movies.find()]
    check = [x for x in check_data if x.get(
        "title") == movie_data.get("title")]
    if check:
        raise HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED,
                            detail=f"Movie data is already available")
    response = await db.movies.insert_one(movie_data)
    logger.info(
        f"Movie data has been updated in DB {str(response.inserted_id)}")
    movie_data = [doc async for doc in db.movies.find({"_id": response.inserted_id})]
    if not movie_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Details Not Found..."
        )
    print(panel.Panel(
        f"Added {movie_data} details to DB...", border_style="green"))
    return movie_data


@router.get("/", response_model=list[MovieResponse])
async def get_all_movies(db=Depends(get_db)):
    movie_data = [doc async for doc in db.movies.find()]
    if not movie_data:
        print(panel.Panel(f"Details Not Found...", border_style="red"))
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Details Not Found..."
        )
    print(panel.Panel(
        f"list of directors - {movie_data}", border_style="green"))
    return movie_data
