from .. import models, schemas, auth_utils, database
from sqlalchemy.orm import Session
from fastapi import (
                    APIRouter,
                    HTTPException,
                    Depends,
                    status
                    )     
from typing import List


router  = APIRouter(
    prefix = "/api/users",
    tags = ['Users']
)
     

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):

    hashed_password = auth_utils.get_password_hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    print(user.password)
    return new_user



@router.get('/{id}', response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"User with id: {id} does not exists")
    
    return user


