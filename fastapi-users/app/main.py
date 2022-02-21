from fastapi import FastAPI
from . import models
from . import database
from .routers import users, auth


models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)