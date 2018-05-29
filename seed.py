from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///../actors.db')

Session = sessionmaker(bind=engine)
session = Session()

# add and commit the actors and roles below
