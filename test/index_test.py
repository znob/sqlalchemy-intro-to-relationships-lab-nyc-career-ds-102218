import unittest, sqlite3, sys
sys.path.insert(0, '..')
from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///actors.db')

Session = sessionmaker(bind=engine)
session = Session()

class TestHasManyBelongsTo(unittest.TestCase):
    bale = Actor(name='Christian Bale')
    paltrow = Actor(name='Gwyneth Paltrow')
    bale.roles = [Role(character='Bruce Wayne'), Role(character='Patrick Bateman'), Role(character='Dr. Michael Burry')]
    paltrow.roles = [Role(character='Pepper Potts')]
    if bool(session.query(Actor).all()) == False:
        session.add(bale)
        session.add(paltrow)
        session.commit()

    test_bale = session.query(Actor).filter_by(name='Christian Bale')[0]
    test_paltrow = session.query(Actor).filter_by(name='Gwyneth Paltrow')[0]

    def test_actor(self):
        self.assertEqual(self.test_bale.name, 'Christian Bale')
        self.assertEqual(self.test_paltrow.name, 'Gwyneth Paltrow')

    def test_actor_has_many_roles(self):
        self.assertEqual(len(self.test_bale.roles), 3)
        self.assertEqual(len(self.test_paltrow.roles), 1)

    def test_roles(self):
        self.assertEqual(session.query(Role).all()[0].character, 'Bruce Wayne')
        self.assertEqual(session.query(Role).all()[1].character, 'Patrick Bateman')
        self.assertEqual(session.query(Role).all()[2].character, 'Dr. Michael Burry')
        self.assertEqual(session.query(Role).all()[3].character, 'Pepper Potts')

    def test_role_belongs_to_actor(self):
        self.assertEqual(self.test_bale, session.query(Role).all()[0].actor)
        self.assertEqual(self.test_bale, session.query(Role).all()[1].actor)
        self.assertEqual(self.test_bale, session.query(Role).all()[2].actor)
        self.assertEqual(self.test_paltrow, session.query(Role).all()[3].actor)
