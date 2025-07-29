from typing import List
from bson import ObjectId
from fastapi import APIRouter, HTTPException, status, Depends
from app.database.db_connection import get_db
from app.schemas.actor_model import ActorModel, ActorResponse
from rich import panel, print
from app.logger.logger import logger
router = APIRouter()


@router.post("/", response_model=List[ActorResponse])
async def create_actor(actor: ActorModel, db=Depends(get_db)):
    actor_data = actor.model_dump()
    check_data = [doc async for doc in db.actors.find()]
    check = [x for x in check_data if x.get("name") == actor_data.get("name")]
    if check:
        raise HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED,
                            detail=f"Actor data is already available")
    actor_data["name"] = actor_data["name"].lower()
    response = await db.actors.insert_one(actor_data)
    logger.info(
        f"Actor data has been updated in DB {str(response.inserted_id)}")
    actor_data_res = [
        doc async for doc in db.actors.find({"_id": response.inserted_id})
    ]
    if not actor_data_res:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Details Not Found..."
        )
    print(panel.Panel(
        f"Added {actor_data_res} details to DB...", border_style="green"))
    return actor_data_res


@router.get("/", response_model=List[ActorResponse])
async def list_actors(db=Depends(get_db)):
    actors_data = [doc async for doc in db.actors.find()]
    if not actors_data:
        print(panel.Panel(f"Details Not Found...", border_style="red"))
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Details Not Found..."
        )
    print(panel.Panel(f"list of actors - {actors_data}", border_style="green"))
    return actors_data
