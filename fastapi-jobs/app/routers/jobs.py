import shutil
from fastapi import (
    
                UploadFile,
                Response, 
                status, 
                HTTPException, 
                Depends, 
                APIRouter
            )
from sqlalchemy.orm import Session
from typing import List
from .. database import get_db
from .. import models
from .. import schemas
from fastapi import UploadFile



router =  APIRouter(

    prefix = "/jobs",
    tags = ["Jobs"]
)



@router.post("/upload-images/")
def create_upload_files(images: List[UploadFile]):

    for image in images:
        with open("media/" + image.filename, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
    return {"images": [file.filename for file in images]}





@router.get("/", response_model=List[schemas.Job])
def get_jobs(db: Session = Depends(get_db)):
    jobs = db.query(models.Job).all()
    return jobs





@router.post("/", status_code=status.HTTP_201_CREATED,  response_model=schemas.Job)
def create_job(job: schemas.JobCreate,  db: Session = Depends(get_db)):


    new_job = models.Job(**job.dict())
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    # print(new_job.id)
    
    return new_job




@router.post("/apply", status_code=status.HTTP_201_CREATED)
def apply_job(applied_job: schemas.ApplyJob, db: Session = Depends(get_db)):
    
    applied_job = models.JobsApplicants(**applied_job.dict())

    job = db.query(models.Job).filter(models.Job.id == applied_job.job_id).first()
    # print(type(applied_job.job_id))
    # print(type(applied_job.user_id))
    # print(job.user_id)
    
    if applied_job.user_id == job.user_id:
        return {"You cannot apply your own job"}
 
    try:

        db.add(applied_job)
        db.commit()
        db.refresh(applied_job)

    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    return applied_job

    




@router.get("/{id}", response_model=schemas.Job)
def get_jobs(id: int, db: Session = Depends(get_db)):
    job = db.query(models.Job).filter(models.Job.id == id).first()
    
    
    if not job:
        raise HTTPException(status_code= 404, detail = f"job with id: {id} was not found")
    return  job






@router.put("/{id}", response_model=schemas.Job)
def update_job(id: int, updated_job: schemas.JobCreate, db: Session = Depends(get_db)):
    job_query = db.query(models.Job).filter(models.Job.id == id)

    job = job_query.first()
    if not job:
        raise HTTPException(f"job with id: {id} does not exist")

    job_query.update(updated_job.dict(), synchronize_session=False)

    db.commit()
    
    return job




@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_job(id:int, db: Session = Depends(get_db)):
    job_query = db.query(models.Job).filter(models.Job.id == id)
    job = job_query.first()
    
    if not job:
        raise HTTPException(f"job with id: {id} does not exist")
    
    job_query.delete(synchronize_session=False)
    db.commit()
   
    return Response(status_code=status.HTTP_204_NO_CONTENT)




