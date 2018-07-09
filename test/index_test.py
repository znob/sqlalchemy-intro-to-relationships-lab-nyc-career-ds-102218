import unittest, sqlite3, sys
sys.path.insert(0, '..')
from models import *
from sqlalchemy import create_engine
sys.path.insert(0, '..')
from queries import *

if bool(session.query(Actor).all()) == False:
    exec(open("./seed.py").read())

class TestHasManyBelongsTo(unittest.TestCase):
    tom = session.query(Actor).filter_by(name='Tom Hanks')[0]
    gwyneth = session.query(Actor).filter_by(name='Gwyneth Paltrow')[0]
    actor_3 = session.query(Actor).all()[2]

    def test_created_three_actors(self):
        self.assertEqual(len(session.query(Actor).all()), 3)

    def test_actors_have_two_roles(self):
        self.assertEqual(len(self.tom.roles), 4)
        self.assertEqual(len(self.gwyneth.roles), 2)
        self.assertEqual(len(self.actor_3.roles), 2)

    def test_created_six_roles(self):
        self.assertEqual(len(session.query(Role).all()), 8)

    def test_roles_belong_to_actor(self):
        self.assertEqual(session.query(Role).filter_by(character='Forrest Gump')[0].actor, self.tom)
        self.assertEqual(session.query(Role).filter_by(character='Woody')[0].actor, self.tom)
        self.assertEqual(session.query(Role).filter_by(character='Jim Lovell')[0].actor, self.tom)
        self.assertEqual(session.query(Role).filter_by(character='Robert Langdon')[0].actor, self.tom)

        self.assertEqual(session.query(Role).filter_by(character='Margot Tenenbaum')[0].actor, self.gwyneth)
        self.assertEqual(session.query(Role).filter_by(character='Pepper Potts')[0].actor, self.gwyneth)


    def test_return_gwyneth_paltrows_roles(self):
        gwyneth_roles = return_gwyneth_paltrows_roles()
        pepper_potts = session.query(Actor).filter_by(name='Gwyneth Paltrow')[0].roles[0].character
        self.assertEqual(gwyneth_roles[0].character, pepper_potts)

        margot = session.query(Actor).filter_by(name='Gwyneth Paltrow')[0].roles[1].character
        self.assertEqual(gwyneth_roles[1].character, margot)

    def test_return_tom_hanks_2nd_role(self):
        tom_second_role = return_tom_hanks_2nd_role()
        self.assertEqual(tom_second_role.character, 'Jim Lovell')
