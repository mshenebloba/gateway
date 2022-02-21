from sysconfig import get_path
from fastapi import UploadFile, File
from pydantic import BaseModel
from datetime import date, datetime
from typing import List
from app.database import Base
import shutil




# Jobs 


class JobBase(BaseModel):
    title: str
    description: str
    price: int
    user_id: int
    category_id: int

    


class Job(JobBase):
    id: int
    created_at: datetime


    class Config:
        orm_mode = True


class JobCreate(JobBase):
    pass

class JobOut(BaseModel):
    Job: Job

    class Config:
        orm_mode = True




class ApplyJob(BaseModel):
    job_id: int
    user_id: int 

    class Config:
        orm_mode = True