import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType
from sqlalchemy.ext.declarative import declarative_base

JobBase = declarative_base()

class Job(JobBase):
    __tablename__ = "job"
    
    id=Column(
        Integer,
        primary_key=True,
        nullable=False
    )

    job_id_external=Column(
        String, 
        nullable=False
    )

    title=Column(
        String,
        nullable=False,
        default="test"
    )
    description=Column(
        Text, 
        nullable=True,
    )

    link=Column(
        String, 
        nullable=True
    )

    date=Column(
        DateTime, 
        default=datetime.datetime.utcnow
    )

    is_posted=Column(
        Boolean, 
        default=False
    )