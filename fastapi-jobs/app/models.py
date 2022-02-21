from sqlalchemy import (
                            Column,
                            Integer,
                            String,                            
                        )

from .database import Base
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy_utils import URLType
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.types import PickleType
from sqlalchemy import UniqueConstraint


class Job(Base):
    __tablename__ = "jobs"
    user_id = Column(Integer, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    image = Column(URLType)
    price = Column(Integer, nullable=False)
    category_id = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))




class JobsApplicants(Base):
    __tablename__ = "jobs_applicants"
    __table_args__ = (UniqueConstraint('job_id', 'user_id', name='applicant_job'),
                     )
    id  = Column(Integer, primary_key=True)
    job_id = Column(Integer, nullable=False, unique=False)
    user_id = Column(Integer, nullable=False, unique=False)
   
