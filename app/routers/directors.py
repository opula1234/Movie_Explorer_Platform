from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from app.database.db_connection import get_db
from app.schemas.director_model import DirectorModel, DirectorResponse
from rich import panel, print
from app.logger.logger import logger
router = APIRouter()


@router.post("/", response_model=list[DirectorResponse])
async def create_director(genre: DirectorModel, db=Depends(get_db)):
    director_data = genre.model_dump()
    check_data = [doc async for doc in db.director.find()]
    check = [x for x in check_data if x.get(
        "name") == director_data.get("name")]
    if check:
        raise HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED,
                            detail=f"Director data is already available")
    director_data["name"] = director_data["name"].lower()
    response = await db.director.insert_one(director_data)
    logger.info(
        f"Director data has been updated in DB {str(response.inserted_id)}")
    director_data = [
        doc async for doc in db.director.find({"_id": response.inserted_id})
    ]
    if not director_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Details Not Found..."
        )
    print(panel.Panel(
        f"Added {director_data} details to DB...", border_style="green"))
    return director_data


@router.get("/", response_model=List[DirectorResponse])
async def get_director(db=Depends(get_db)):
    director_data = [doc async for doc in db.director.find()]
    if not director_data:
        print(panel.Panel(f"Details Not Found...", border_style="red"))
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Details Not Found..."
        )
    print(panel.Panel(
        f"list of directors - {director_data}", border_style="green"))
    return director_data
