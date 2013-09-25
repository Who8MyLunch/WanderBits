#!/usr/bin/python

from __future__ import division, print_function, unicode_literals


import os
import sys
import unittest

from context import wanderbits

import cStringIO as StringIO

class Test_Executive(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_does_it_init(self):
        E = wanderbits.executive.Executive()


    #############################################
    # Reading and writing text.
    def test_read_two_lines(self):
        line_1 = 'hello to the test'
        line_2 = 'good day to the world!'
        lines = '{:s}\n{:s}\n'.format(line_1, line_2)

        buff_in = StringIO.StringIO(lines)
        buff_out = StringIO.StringIO()

        E = wanderbits.executive.Executive(stdin=buff_in, stdout=buff_out)

        line_a = E.console_read()
        line_b = E.console_read()

        self.assertTrue(line_1 == line_a)
        self.assertTrue(line_2 == line_b)


    def test_write_two_lines(self):
        line_1 = 'hello to the test'
        line_2 = 'good day to the world!'
        lines = '{:s}\n{:s}\n'.format(line_1, line_2)

        buff_in = StringIO.StringIO()
        buff_out = StringIO.StringIO()

        E = wanderbits.executive.Executive(stdin=buff_in, stdout=buff_out)

        E.console_write(line_1)
        self.assertTrue(buff_out.getvalue() == line_1 + '\n')

        E.console_write(line_2)
        self.assertTrue(buff_out.getvalue() == line_1 + '\n' + line_2 + '\n')


    def test_read_generator(self):
        line_1 = 'hello to the test'
        line_2 = 'good day to the world!'
        lines = '{:s}\n{:s}\n'.format(line_1, line_2)

        buff_in = StringIO.StringIO(lines)
        buff_out = StringIO.StringIO()

        E = wanderbits.executive.Executive(stdin=buff_in, stdout=buff_out)

        lines_work = ''
        for k, line in enumerate(E.console_reader()):
            if k >= 4:
                raise ValueError('Should have stopped before now')

            if len(line):
                lines_work += line + '\n'
            else:
                break

        self.assertTrue(lines == lines_work)



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
