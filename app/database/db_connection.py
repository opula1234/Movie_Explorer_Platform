from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from rich import print, panel
import os


# Development - Local

# MONGO_URL: str = "mongodb://localhost:27017"
# client = AsyncIOMotorClient(MONGO_URL)

# Development - Container

MONGO_URL: str = os.getenv("MONGO_URI", "mongodb://mongo:27017")
client = AsyncIOMotorClient(MONGO_URL)

db = client.movie_backend


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.mongodb_client = AsyncIOMotorClient(MONGO_URL)
    app.mongodb = app.mongodb_client.movie_backend
    print(panel.Panel("Connected to MongoDB...", border_style="green"))

    try:
        yield
    finally:
        app.mongodb_client.close()
        print(panel.Panel("Disconnected to MongoDB...", border_style="green"))


def get_db(request: Request):
    return request.app.mongodb
