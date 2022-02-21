from fastapi import FastAPI
from sqlalchemy import (
                       Column,
                       Integer,
                       
                    )

from .database import Base 
from sqlalchemy import UniqueConstraint




class JobRatings(Base):
    __tablename__ = "job_ratings"
    __table_args__ = (UniqueConstraint('job_id', 'user_id', name='for_job_rating'),
                     )

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, nullable=False)
    job_id = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=False)



class UserRatings(Base):
    __tablename__ = "user_ratings"
    __table_args__ = (UniqueConstraint('job_id', 'user_id', name='for_user_rating'),
                     )

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, nullable=False)
    job_id = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=False)