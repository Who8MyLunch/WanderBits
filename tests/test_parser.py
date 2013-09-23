#!/usr/bin/python

from __future__ import division, print_function, unicode_literals


import os
import time
import unittest

from context import wanderbits


class Test_Parser(unittest.TestCase):

    def setUp(self):
        self.parser = wanderbits.line_parser.Parser()

    def tearDown(self):
        pass


    def test_does_it_run(self):
        line = 'go north'
        tokens = self.parser.parse(line)


    def test_does_it_parse(self):
        line = 'put cat dog'
        tokens = self.parser.parse(line)

        tokens_true = ['put', 'cat', 'dog']

        self.assertTrue(len(tokens) == len(tokens_true))
        for u, v in zip(tokens, tokens_true):
            msg = u + ' != ' + v
            self.assertTrue(u == v, msg)


    def test_punctuation(self):
        line = '.,;put cat!?,..dog! ,.?!;:-+[]{}'
        tokens = self.parser.parse(line)

        tokens_true = ['put', 'cat', 'dog']

        self.assertTrue(len(tokens) == len(tokens_true))
        for u, v in zip(tokens, tokens_true):
            msg = u + ' != ' + v
            self.assertTrue(u == v, msg)


    def test_ignore_words(self):
        line = 'put the cat on the dog'
        tokens = self.parser.parse(line)

        tokens_true = ['put', 'cat', 'dog']

        self.assertTrue(len(tokens) == len(tokens_true))
        for u, v in zip(tokens, tokens_true):
            msg = u + ' != ' + v
            self.assertTrue(u == v, msg)




# Standalone.
if __name__ == '__main__':
    unittest.main(verbosity=2)
