from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from app.database.db_connection import get_db
from app.schemas.movies_model import MovieResponse
from typing import Optional
from rich import panel, print

router = APIRouter()


@router.get("/{actor}/movies", response_model=List[MovieResponse])
async def get_movies_actor(actor: str, db=Depends(get_db)):
    movies_data = [doc async for doc in db.movies.find({"cast": actor})]
    if not movies_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Details Not Found..."
        )
    print(panel.Panel(f"{movies_data}", border_style="green"))
    return movies_data


@router.get("/{genre}/genres", response_model=List[MovieResponse])
async def get_movies_genre(genre: str, db=Depends(get_db)):
    genres_data = [doc async for doc in db.movies.find({"genres": genre})]
    if not genres_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Details Not Found..."
        )
    print(panel.Panel(f"{genres_data}", border_style="green"))
    return genres_data


@router.get("/", response_model=List[MovieResponse])
async def get_movies_by_input(
    genre: Optional[str] | None = None,
    actor: Optional[str] | None = None,
    release_year: Optional[int] | None = None,
    director: Optional[str] | None = None,
    db=Depends(get_db),
):

    query = {}

    if genre:
        query["genres"] = {"$in": [genre]}
    if actor:
        query["cast"] = {"$in": [actor]}
    if release_year:
        query["released_year"] = {"$in": [release_year]}
    if director:
        query["director"] = {"$in": [director]}

    movies_data = [doc async for doc in db.movies.find(query)]

    print(panel.Panel(f"{movies_data}", border_style="green"))

    return movies_data
