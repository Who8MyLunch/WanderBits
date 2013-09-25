#!/usr/bin/python

from __future__ import division, print_function, unicode_literals


import os
import time
import unittest

from context import wanderbits


class Test_Parser(unittest.TestCase):

    def setUp(self):
        action_name = ['put', 'go']
        self.parser = wanderbits.line_parser.Parser(action_name)

    def tearDown(self):
        pass


    def test_does_it_run(self):
        line = 'go north'
        results = self.parser.parse(line)


    def test_input_actions_string(self):

        action_name = 'go'  # earlier this would have caused a problem as action_name is a string, not a list.  Parser now should handle both.
        parser = wanderbits.line_parser.Parser(action_name)

        line = 'go north'
        results = parser.parse(line)


    def test_input_actions_list(self):

        action_name = ['go']  # earlier this would have caused a problem as action_name is a string, not a list.  Parser now should handle both.
        parser = wanderbits.line_parser.Parser(action_name)

        line = 'go north'
        results = parser.parse(line)


    def test_does_it_parse(self):
        line = 'put cat dog'
        name, args = self.parser.parse(line)

        name_true = 'put'
        args_true = ['cat', 'dog']

        self.assertTrue(name == name_true)
        self.assertTrue(len(args) == len(args_true))

        for u, v in zip(args, args_true):
            msg = u + ' != ' + v
            self.assertTrue(u == v, msg)


    def test_punctuation(self):
        line = '.,;put cat!?,..dog! ,.?!;:-+[]{}'
        name, args = self.parser.parse(line)

        name_true = 'put'
        args_true = ['cat', 'dog']

        self.assertTrue(name == name_true)
        self.assertTrue(len(args) == len(args_true))

        for u, v in zip(args, args_true):
            msg = u + ' != ' + v
            self.assertTrue(u == v, msg)


    def test_ignore_words(self):
        line = 'put the cat on the dog'
        name, args = self.parser.parse(line)

        name_true = 'put'
        args_true = ['cat', 'dog']

        self.assertTrue(name == name_true)
        self.assertTrue(len(args) == len(args_true))

        for u, v in zip(args, args_true):
            msg = u + ' != ' + v
            self.assertTrue(u == v, msg)


    def test_invalid_action(self):
        line = 'run away from the error!'  # action run is not known.

        with self.assertRaises(wanderbits.errors.ParserError):
            name, args = self.parser.parse(line)




# Standalone.
if __name__ == '__main__':
    unittest.main(verbosity=2)
