#!/usr/bin/python

from __future__ import division, print_function, unicode_literals

"""
Executive class for WanderBits, a text-based adventure game.
"""

import sys

import errors
import console
import line_parser


class Executive(object):
    """
    Executive class for WanderBits, a text-based adventure game.
    """

    def __init__(self, options=None, stdin=None, stdout=None):
        """
        Initialize Executive class instance.

        stdin, stdout: default to sys.stdin and sys.stdout
        """

        if stdin:
            self.stdin = stdin
        else:
            self.stdin = sys.stdin

        if stdout:
            self.stdout = stdout
        else:
            self.stdout = sys.stdout

        actions = ['go', 'quit', 'exit']
        self.parser = line_parser.Parser(actions)

        # Done.



    def console_read(self):
        """
        Read a line of text from the user.  Block until user hits enter.
        Also handle nice display of command prompt.
        """
        self.stdout.write('\n> ')
        line = self.stdin.readline()

        return line.strip()



    def console_reader(self):
        """
        A generator to yield user's lines of text to the caller.
        """
        try:
            while True:
                yield self.console_read()

        except KeyboardInterrupt:
            # catch when the user hits ctrl-c at the prompt.
            # Yield exit command.
            yield 'exit'

        # Done.



    def console_write(self, text):
        """
        Write some text out to the user.
        """
        output = '{:s}\n'.format(text)

        self.stdout.write(output)



    def start(self):
        """
        Start running the Executive's event loop.  Block until user's game session is finished.
        """

        # Main loop.
        self.console_write('\nWelcome\n')
        for line in self.console_reader():

            # Parse new line of text.
            action_name, arguments = self.parser.parse(line)

            # Take action!

            # Send response to user.
            response = 'hello!!!! ' + action_name
            self.console_write(response)


        # Clean up, save game state, exit.
        # Save game state.
        self.console_write('Exit!\nSaving game state...')

        # TODO: save game info.

        # End the game nicely.
        self.console_write('Bye.\n')






if __name__ == '__main__':


    E = Executive()
    E.start()

