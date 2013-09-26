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

    def __init__(self, actions, punctuation=None, ignore_words=None):
        """
        Initialize text parser.

        actions: list of valid game Action names.
        punctation: (optional) string of punctation characters that will be
                     ignored.
        ignore_words: (optional) list of words to ignore
        """

        if issubclass(type(actions), basestring):
            actions = [actions]

        self.actions = [a.lower() for a in actions]

        if not punctuation:
            self.punctuation = ',.?!;:-+[]{}'

        if not ignore_words:
            self.ignore_words = ['a', 'the', 'at', 'or', 'in', 'on',
                                 'to', 'too', 'eh', 'me', 'my']

        # Done.

    def parse(self, line):
        """
        line: a line of text entered by the user.

        Parse a line of text into tokens that represent game verbs and nouns.
        Tokens are constructed from contiguous sets of letters and numbers.
        Whitespace and punctuation demark boundaries between tokens.
        """

        if not issubclass(type(line), basestring):
            raise errors.ParserError('Input line argument must be string or' +
                                     'unicode: {:s}'.format(str(line)))

        # Carve out the tokens.
        tokens = self.chop_words(line)

        # Remove ignore words from token list.
        tokens = self.remove_ignore_words(tokens)

        # Regroup tokens into an action name followed by one or more action
        # arguments.
        action_name, action_arguments = tokens[0], tokens[1:]

        # Valid action?
        if action_name not in self.actions:
            msg = 'The word "{:s}" is not a valid action.'.format(action_name)
            raise errors.ParserError(msg)

        # Done.
        return action_name, action_arguments

    def chop_words(self, line):
        """
        Chop user-supplied string into tokens.
        Ignore punctuation.
        """
        # Force lowercase.
        line = line.lower()

        # Replace punctation characters by a space.
        for p in self.punctuation:
            line = line.replace(p, ' ')

        tokens = line.split()

        # Done.
        return tokens

    def remove_ignore_words(self, tokens):
        """
        Make sure sequence of tokens begins with a known Action.
        If tokens exist after the Action, assume they are valid.  Proper
        checking of Things must happen outside this class.

        Also, reject as tokens any words that match with anything on the
        ignore list.
        """

        for w in self.ignore_words:
            while w in tokens:
                tokens.remove(w)

        # Done.
        return tokens
