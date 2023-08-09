from sqlalchemy import Column, Boolean,Integer,String
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True,index=True)
    username = Column(String(50),unique=True)

class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String(50))
    content = Column(String(200))
    user_id = Column(Integer)
