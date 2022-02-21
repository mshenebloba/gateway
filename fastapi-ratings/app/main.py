from fastapi import FastAPI
from .import models
from .database import engine
from .routers import ratings


models.Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(ratings.router)