from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///actors.db')

Session = sessionmaker(bind=engine)
session = Session()

# add and commit the actors and roles below
tom = Actor(name='Tom Hanks')
paltrow = Actor(name='Gwyneth Paltrow')
bale = Actor(name='Christian Bale')
tom.roles = [Role(character='Forrest Gump'), Role(character='Jim Lovell'), Role(character='Woody'),Role(character='Robert Langdon')]
paltrow.roles = [Role(character='Pepper Potts'), Role(character='Margot Tenenbaum')]
bale.roles = [Role(character='Bruce Wayne'), Role(character='Dr. Michael Burry')]

session.add_all([tom, paltrow, bale])
session.commit()
