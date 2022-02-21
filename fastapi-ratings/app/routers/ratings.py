import http
from http.client import HTTPException
from fastapi import (
                     Response,
                     status,
                     Depends,
                     APIRouter   
                    )
from sqlalchemy.orm import Session
from .. import models
from .. database import get_db
from .. import schemas
from typing import List


router = APIRouter(
    prefix = "/ratings",
    tags = ["Ratings"]
)


@router.post("/job", status_code=status.HTTP_201_CREATED)
def job_rating(rating: schemas.JobRating, db: Session = Depends(get_db)):
    
    rated_job = models.JobRatings(**rating.dict())

    # rating_query = db.query(models.Ratings).filter(models.Ratings.user_id == rating.user_id)

 
    try:

        db.add(rated_job)
        db.commit()
        db.refresh(rated_job)

    except:
        
        return Response("You cannot rate job twice")
        

    return rated_job



@router.post("/user", status_code=status.HTTP_201_CREATED)
def user_rating(user_rating: schemas.UserRating, db: Session = Depends(get_db)):

    rated_user = models.UserRatings(**user_rating.dict())

    try:

        db.add(rated_user)
        db.commit()
        db.refresh(rated_user)

    except:
        
        return Response("You cannot rate user twice")
        

    return rated_user





@router.get("/users", response_model = List[schemas.UserRating])
def get_user_ratings(db: Session = Depends(get_db)):
    user_ratings = db.query(models.UserRatings).all()

    return user_ratings





@router.get("/jobs", response_model = List[schemas.JobRating])
def get_job_ratings(db: Session = Depends(get_db)):
    job_ratings = db.query(models.JobRatings).all()

    return job_ratings