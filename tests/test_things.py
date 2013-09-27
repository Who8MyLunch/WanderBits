#!/usr/bin/python

from __future__ import division, print_function, unicode_literals

import unittest

from context import wanderbits


class Test_Things(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # def test_does_it_init(self):
    #     wanderbits.actions.Look()
    #     wanderbits.actions.Go()
    #     wanderbits.actions.Take()
    #     wanderbits.actions.Put()
    #     wanderbits.actions.Quit()

    # def test_init_abc(self):
    #     self.assertRaises(TypeError, wanderbits.actions)

    # def test_property_name(self):
    #     A = wanderbits.actions.Look()
    #     self.assertTrue('look' in A.names)

    # def test_property_description(self):
    #     d = 'hello a test is here'
    #     A = wanderbits.actions.Look(description=d)
    #     self.assertTrue(A.description == d)


# Standalone.
if __name__ == '__main__':
    unittest.main(verbosity=2)
