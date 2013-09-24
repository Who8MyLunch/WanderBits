#!/usr/bin/python

from __future__ import division, print_function, unicode_literals

"""
Console class for WanderBits, a text-based adventure game.
"""

import sys

import errors


class Console(object):
    """
    Console class for WanderBits, a text-based adventure game.
    """
    def __init__(self, stdin=None, stdout=None):
        """
        Initialize a console instance.
        """
        if not stdin:
            stdin = sys.stdin

        if not stdout:
            stdout = sys.stdout

        self.stdin = stdin
        self.stdout = stdout

        # Done.


    def readline(self):
        """
        Read a line of text from the user.  Block until user hits enter.
        """
        self.stdout.write('\n > ')
        line = self.stdin.readline()

        return line.strip()


    def write(self, text):
        """
        Write some text out to the user.
        """

        output = '\n{:s}'.format(text)

        self.stdout.write(output)
