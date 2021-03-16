from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
import datetime

Base = declarative_base()

class Files(Base):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(150))
    filelink = Column(String(150))
    created_at =  Column(DateTime, default=datetime.datetime.utcnow)
    