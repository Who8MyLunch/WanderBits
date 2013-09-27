#!/usr/bin/python

from __future__ import division, print_function, unicode_literals

import unittest

from context import wanderbits


class Test_Action(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_does_it_init(self):
        user_placeholder = 'asdasd'
        wanderbits.actions.Look(user_placeholder)
        wanderbits.actions.Go(user_placeholder)
        wanderbits.actions.Take(user_placeholder)
        wanderbits.actions.Put(user_placeholder)
        wanderbits.actions.Quit(user_placeholder)

    def test_init_abc(self):
        self.assertRaises(TypeError, wanderbits.actions.Action)

    def test_property_name(self):
        user_placeholder = 'asdasd'
        A = wanderbits.actions.Look(user_placeholder)
        self.assertTrue('look' in A.names)

    def test_property_description(self):
        user_placeholder = 'asdasd'
        d = 'hello a test is here'
        A = wanderbits.actions.Look(user_placeholder, description=d)
        self.assertTrue(A.description == d)

    def test_apply(self):
        pass  # 1/0

# Standalone.
if __name__ == '__main__':
    unittest.main(verbosity=2)
