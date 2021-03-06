#!/usr/bin/python

from __future__ import division, print_function, unicode_literals

import os
import unittest

from context import wanderbits


class Test_Things(unittest.TestCase):

    def setUp(self):
        path_module = os.path.dirname(os.path.abspath(__file__))
        f = os.path.join(path_module, '..', 'wanderbits', 'game.yml')
        self.game_info = wanderbits.config.read(f)

    def tearDown(self):
        pass

    def test_does_room_init(self):
        info = self.game_info['rooms'][0]
        wanderbits.things.Room(**info)

    def test_does_item_init(self):
        info = self.game_info['items'][0]
        wanderbits.things.Item(**info)

    def test_does_user_init(self):
        info = self.game_info['user'][0]
        wanderbits.things.User(**info)

    def test_find_things(self):
        name = 'apple'
        many_things = [wanderbits.things.Item(**info) for
                       info in self.game_info['items']]
        wanderbits.things.find_thing(many_things, name)

    def test_init_abc(self):
        # Should not be able to instanciate an abstract class.
        self.assertRaises(TypeError, wanderbits.things.Thing)

    #############################################
    # Test for property values.
    def test_property_name(self):
        info = self.game_info['rooms'][0]
        A = wanderbits.things.Room(**info)
        self.assertTrue('kitchen' in A.name)

    def test_property_description(self):
        info = self.game_info['rooms'][0]
        A = wanderbits.things.Room(**info)
        txt = 'a very tidy average-looking kitchen'
        self.assertTrue(A.description == txt)

    def test_property_size(self):
        info = self.game_info['rooms'][0]
        A = wanderbits.things.Room(**info)
        self.assertTrue(A.size == 1000)

    def test_property_capacity(self):
        info = self.game_info['rooms'][0]
        A = wanderbits.things.Room(**info)
        self.assertTrue(A.capacity == 1000)

    #############################################
    # Test for container actions.
    def test_add_is_container(self):
        info_apple = self.game_info['items'][0]
        A = wanderbits.things.Item(**info_apple)

        info_sack = self.game_info['items'][1]
        B = wanderbits.things.Item(**info_sack)

        # Put the apple in the sack.
        B.add(A)

        self.assertTrue(A in B.container)

    def test_add_item_twice(self):
        info_apple = self.game_info['items'][0]
        A = wanderbits.things.Item(**info_apple)

        info_sack = self.game_info['items'][1]
        B = wanderbits.things.Item(**info_sack)

        # Put the apple in the sack.
        B.add(A)

        # B.add(A)
        # Put the apple in the sack again.  I know!  This is a dumb rule!
        self.assertRaises(wanderbits.errors.ThingError, B.add, A)

    def test_add_is_not_container(self):
        info_apple = self.game_info['items'][0]
        A = wanderbits.things.Item(**info_apple)

        info_sack = self.game_info['items'][1]
        B = wanderbits.things.Item(**info_sack)

        # Put the sack in the apple.
        # A.add(B)
        self.assertRaises(wanderbits.errors.ThingError, A.add, B)

    def test_available_space_init(self):
        info_sack = self.game_info['items'][1]
        B = wanderbits.things.Item(**info_sack)

        self.assertTrue(B.available_space == 100)

    def test_available_space_after_add(self):
        info_apple = self.game_info['items'][0]
        A = wanderbits.things.Item(**info_apple)

        info_sack = self.game_info['items'][1]
        B = wanderbits.things.Item(**info_sack)

        B.add(A)
        self.assertTrue(B.available_space == 99)

    def test_remove(self):
        info_apple = self.game_info['items'][0]
        A = wanderbits.things.Item(**info_apple)

        info_sack = self.game_info['items'][1]
        B = wanderbits.things.Item(**info_sack)

        B.add(A)
        self.assertTrue(A in B.container)

        B.remove(A)
        self.assertTrue(A not in B.container)

        # B.remove(A)
        self.assertRaises(wanderbits.errors.ThingError, B.remove, A)

    #############################################
    # User as a container.
    def test_user_local_things(self):
        E = wanderbits.executive.Executive(self.game_info)

        info_apple = self.game_info['items'][0]
        A = wanderbits.things.Item(**info_apple)

        info_sack = self.game_info['items'][1]
        B = wanderbits.things.Item(**info_sack)

        info_room = self.game_info['rooms'][0]
        C = wanderbits.things.Item(**info_room)

        info_rock = self.game_info['items'][2]
        D = wanderbits.things.Item(**info_rock)

        self.assertTrue(A.name in [n.name for n in E.user.local_things])
        self.assertTrue(B.name in [n.name for n in E.user.local_things])
        self.assertTrue(C.name in [n.name for n in E.user.local_things])
        self.assertFalse(D.name in [n.name for n in E.user.local_things])

# Standalone.
if __name__ == '__main__':
    unittest.main(verbosity=2)
