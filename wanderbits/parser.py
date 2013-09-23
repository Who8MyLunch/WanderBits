#!/usr/bin/python

from __future__ import division, print_function, unicode_literals

"""
Parser class for WanderBits, a text-based adventure game.
"""

import errors


class Parser(object):
    """
    Parser class for WanderBits, a text-based adventure game.
    """

    def __init__(self, punctuation=None, ignore_words=None):
        """
        Initialize parser with known game actions and game things.

        Errors will result in raising a ParserError exception whose message value will be
        suitable for display direct to the user console.
        """
        if not punctuation:
            self.punctuation = ',.?!;:-+[]{}'

        if not ignore_words:
            self.ignore_words = ['a', 'the', 'at', 'or', 'in', 'on', 'to', 'too', 'eh', 'me', 'my']

        # Done.



    # def work(self, line):
    #     """
    #     Do a unit of work for the good of the game.
    #     Accept a line of text that was originally entered by the user.
    #     Return a tuple of results: (action_name, list_of_things).
    #     Raise a ParserError exception if there is a problem.
    #     """
    #     tokens = self.parse(line)
    #     # action, things = self.validate(tokens)
    #     # Done.
    #     return tokens



    def parse(self, line):
        """
        line: a line of text entered by the user.

        Parse a line of text into tokens that represent game verbs and nouns.  Tokens are
        constructed from contiguous sets of letters and numbers.  Whitespace and punctuation
        demark boundaries between tokens.
        """

        if not issubclass(type(line), basestring):
            raise errors.ParserError('Input line argument must be string or unicode: {:s}'.format(str(line)))

        # Force lowercase.
        line = line.lower()

        # Replace punctation characters by a space.
        for p in self.punctuation:
            line = line.replace(p, ' ')

        # Carve out the tokens.
        tokens = line.split()

        # Remove ignore words from token list.
        tokens = self.validate(tokens)

        # Done.
        return tokens



    def validate(self, tokens):
        """
        Make sure sequence of tokens begins with a known Action.
        If tokens exist after the Action, make sure they are valid Things.
        Also, reject as tokens any words that match with anything on the ignore list.
        """

        for w in self.ignore_words:
            while w in tokens:
                tokens.remove(w)

        # Done.
        return tokens
