#!/usr/bin/python

from __future__ import division, print_function, unicode_literals


import os
import sys
import unittest

from context import wanderbits

import cStringIO as StringIO

class Test_Console(unittest.TestCase):

    def setUp(self):
        self.line_0 = 'hello to the test'
        self.line_1 = 'good day to the world!'

    def tearDown(self):
        pass


    def test_does_it_init(self):
        console = wanderbits.console.Console()


    def test_read_two_lines(self):
        lines = '{:s}\n{:s}\n'.format(self.line_0, self.line_1)

        stdin = StringIO.StringIO(lines)

        console = wanderbits.console.Console(stdin=stdin)

        line_0 = console.readline()
        line_1 = console.readline()

        self.assertTrue(line_0 == self.line_0)
        self.assertTrue(line_1 == self.line_1)


    def test_write_two_lines(self):
        pass

    # def test_does_it_parse(self):
    #     line = 'put cat dog'
    #     tokens = self.parser.parse(line)

    #     tokens_true = ['put', 'cat', 'dog']

    #     self.assertTrue(len(tokens) == len(tokens_true))
    #     for u, v in zip(tokens, tokens_true):
    #         msg = u + ' != ' + v
    #         self.assertTrue(u == v, msg)





# Standalone.
if __name__ == '__main__':
    unittest.main(verbosity=2)
