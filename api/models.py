from sqlalchemy import Column, Integer, String
from sql_app.database import Base

class UserInfo(Base):
    __tablename__ = "user_info"

    id = Column(Integer, primary_key=True, index=True)
    fileName = Column(String, unique=True)
    fileLink = Column(String)
    fullname = Column(String, unique=True)