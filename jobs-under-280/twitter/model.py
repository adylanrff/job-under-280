import datetime
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from db import Base

class Tweet(Base):
    __tablename__ = "tweet"

    id = Column(
        Integer,
        primary_key=True,
        nullable=False
        )

    job_id = Column(
        Integer, 
        ForeignKey('job.id'),
        nullable=True
    )

    tweet_date = Column(
        DateTime,
        default=datetime.datetime.now
    )
