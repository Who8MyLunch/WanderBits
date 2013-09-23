#!/usr/bin/python

from __future__ import division, print_function, unicode_literals


import os
import time
import unittest

from context import wanderbits


class Test_Parser_Basic(unittest.TestCase):

    def setUp(self):
        self.parser = wanderbits.parser.Parser()

    def tearDown(self):
        pass


    def test_does_it_run(self):
        line = 'go north'
        tokens = self.parser.parse(line)



    def test_two(self):
        fname = 's'#os.path.join(path_data, 'Lena.dat')
        # data, meta = io.read(fname)
        # self.assertTrue(data.shape == (512, 512, 3))


# Standalone.
if __name__ == '__main__':
    unittest.main(verbosity=2)
