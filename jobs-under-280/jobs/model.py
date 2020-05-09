import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType
from db import Base

class Job(Base):
    __tablename__ = "job"
    
    id=Column(
        Integer,
        primary_key=True,
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
        default="test"
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