from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATA_BASE = "mysql+pymysql://root:kiuf2021@localhost:3306/postblog"

engine = create_engine(URL_DATA_BASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base = declarative_base()