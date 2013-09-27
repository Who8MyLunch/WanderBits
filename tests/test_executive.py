#!/usr/bin/python

from __future__ import division, print_function, unicode_literals


import unittest

from context import wanderbits

import cStringIO as StringIO


class Test_Executive(unittest.TestCase):

    def setUp(self):
        f = '../wanderbits/game.yml'
        self.game_info = wanderbits.config.read(f)

    def tearDown(self):
        pass

    def test_does_it_init(self):
        wanderbits.executive.Executive(self.game_info)

    #############################################
    # Reading and writing text.
    def test_read_two_lines(self):
        line_1 = 'hello to the test'
        line_2 = 'good day to the world!'
        lines = '{:s}\n{:s}\n'.format(line_1, line_2)

        buff_in = StringIO.StringIO(lines)
        buff_out = StringIO.StringIO()

        E = wanderbits.executive.Executive(self.game_info,
                                           stdin=buff_in, stdout=buff_out)

        line_a = E.console_read()
        line_b = E.console_read()

        self.assertTrue(line_1 == line_a)
        self.assertTrue(line_2 == line_b)

    def test_write_two_lines(self):
        line_1 = 'hello to the test'
        line_2 = 'good day to the world!'

        buff_in = StringIO.StringIO()
        buff_out = StringIO.StringIO()

        E = wanderbits.executive.Executive(self.game_info,
                                           stdin=buff_in, stdout=buff_out)

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

        E = wanderbits.executive.Executive(self.game_info,
                                           stdin=buff_in, stdout=buff_out)

        lines_work = ''
        for k, line in enumerate(E.console_reader()):
            if k >= 4:
                raise ValueError('Should have stopped before now')

            if len(line):
                lines_work += line + '\n'
            else:
                break

        self.assertTrue(lines == lines_work)

    #############################################
    # Test ingesting game detail
    def test_ingest_data(self):
        E = wanderbits.executive.Executive(self.game_info)

        self.assertTrue(len(E._rooms) == 6)
        self.assertTrue(len(E._items) == 4)
        self.assertTrue(len(E._actions) == 6)

    def test_ingested_types(self):
        E = wanderbits.executive.Executive(self.game_info)

        self.assertIsInstance(E._user, wanderbits.things.User)
        self.assertIsInstance(E._rooms[0], wanderbits.things.Room)
        self.assertIsInstance(E._items[0], wanderbits.things.Item)
        self.assertIsInstance(E._actions[0], wanderbits.actions.Action)

    #############################################
    # Test game actions.
    def test_find_action(self):
        E = wanderbits.executive.Executive(self.game_info)

        a = E.find_action('go')
        self.assertIsInstance(a, wanderbits.actions.Action)

        a = E.find_action('go')
        self.assertIsInstance(a, wanderbits.actions.Action)

        self.assertRaises(wanderbits.errors.ExecutiveError,
                          E.find_action, 'asdasd')


# Standalone.
if __name__ == '__main__':
    unittest.main(verbosity=2)
