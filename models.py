from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


# write the Role and Actor classes below







engine = create_engine('sqlite:///actors.db')
Base.metadata.create_all(engine)
