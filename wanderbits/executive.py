#!/usr/bin/python

from __future__ import division, print_function, unicode_literals

"""
Executive class for WanderBits, a text-based adventure game.
"""

import errors
import console
import line_parser



class Executive(object):
    """
    Executive class for WanderBits, a text-based adventure game.
    """

    def __init__(self, options=None):
        """
        Initialize Executive class instance.
        """

        self.console = console.Console()
        self.parser = line_parser.Parser()

        # Done.


    def start(self):
        """
        Start running the Executive's event loop.  Block until user's game session is finished.
        """

        keep_looping = True
        while keep_looping:

            try:
                # Line of text from user.
                line = self.console.readline()

                # Do something with text.
                response = 'hello!!!! ' + line

                # Send response to user.
                self.console.write(response)

            except KeyboardInterrupt:
                # Save game state.
                self.console.write('User stop!')
                self.console.write('Saving game state...')

                # TODO: save game info.

                # End the game nicely.
                self.console.write('Bye.\n')
                keep_looping = False


if __name__ == '__main__':
    pass

