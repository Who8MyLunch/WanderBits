#!/usr/bin/python

from __future__ import division, print_function, unicode_literals

import unittest

from context import wanderbits


class Test_Things(unittest.TestCase):

    def setUp(self):
        f = 'test_config.yml'
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
        self.assertRaises(TypeError, wanderbits.things.Thing)

    def test_property_name(self):
        info = self.game_info['rooms'][0]
        A = wanderbits.things.Room(**info)
        self.assertTrue('kitchen' in A.name)

    def test_property_description(self):
        info = self.game_info['rooms'][0]
        A = wanderbits.things.Room(**info)
        txt = 'An average-looking kitchen.  It looks very tidy'
        self.assertTrue(A.description == txt)

    def test_property_size(self):
        info = self.game_info['rooms'][0]
        A = wanderbits.things.Room(**info)
        self.assertTrue(A.size == 1000)

    def test_property_capacity(self):
        info = self.game_info['rooms'][0]
        A = wanderbits.things.Room(**info)
        self.assertTrue(A.capacity == 1000)

    def test_add_is_container(self):
        info_apple = self.game_info['items'][0]
        A = wanderbits.things.Item(**info_apple)

        info_sack = self.game_info['items'][1]
        B = wanderbits.things.Item(**info_sack)

        B.add(A)

    def test_remove(self):
        pass  # 1/0


# Standalone.
if __name__ == '__main__':
    unittest.main(verbosity=2)
