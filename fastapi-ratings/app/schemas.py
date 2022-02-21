from pydantic import BaseModel, conint
from datetime import datetime

class Rating(BaseModel):

    job_id: int
    user_id: int
    rating: int
    # dir: conint(le=1)


class JobRating(Rating):
    pass

    class Config:
        orm_mode = True

class UserRating(Rating):
    pass

    class Config:
        orm_mode = True

