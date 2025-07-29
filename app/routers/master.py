from fastapi import APIRouter

from .genres import router as genre_router
from .actors import router as actor_router
from .directors import router as director_router
from .movies import router as movies_router
from .filter_api import router as filter_api

master_router = APIRouter(prefix="/api")

master_router.include_router(genre_router, prefix="/genres", tags=["Genres"])

master_router.include_router(actor_router, prefix="/actors", tags=["Actors"])


master_router.include_router(director_router, prefix="/directors", tags=["Directors"])


master_router.include_router(movies_router, prefix="/movies", tags=["Movies"])

master_router.include_router(
    filter_api, prefix="/filter", tags=["Filter By Movies, Genres, director and inputs"]
)

__all__ = ["master_router"]
