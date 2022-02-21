from fastapi import FastAPI
from .import models
from .database import engine
from .routers import jobs
from .config import settings


# Creates tables in the database 
#Since there is only table method is commented out

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(jobs.router)


