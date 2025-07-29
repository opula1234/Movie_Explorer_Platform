from fastapi import FastAPI
from app.routers.master import master_router
from .database.db_connection import lifespan
import os
from .logger.logger import logger

app = FastAPI(
    title="Movie Explorer Platform",
    version="1.0",
    description="Movie Explorer Platform is a web app "
    "that lets users explore a rich database of movies, actors, directors, and genres. "
    "It offers detailed film info, supports dynamic filters, "
    "and allows easy navigation through movie-related data.",
    lifespan=lifespan,
)


app.include_router(master_router)


@app.get("/")
async def root():
    logger.info("API Endpoint accessed...")
    return {f"message": "FastAPI is running!. please check swagger page by - {http://localhost:8000/docs}"}
