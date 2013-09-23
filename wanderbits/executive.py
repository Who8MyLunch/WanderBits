#!/usr/bin/python

from __future__ import division, print_function, unicode_literals

"""
Executive class for WanderBits, a text-based adventure game.
"""

import errors


class Executive(object):
    """
    Executive class for WanderBits, a text-based adventure game.
    """

    def __init__(self):
        """
        Initialize Executive class instance.
        """
        pass



    def validate(self, tokens):
        """
        Make sure sequence of tokens begins with a known Action.
        If tokens exist after the Action, make sure they are valid Things.
        Also, reject as tokens any words that match with anything on the ignore list.
        """
        for w in self.ignore_words:
            if w in tokens:
                tokens.remove(w)

        action = tokens[0]
        if not action.lower() in self.game_actions:
            raise errors.ParserError('The word {:s} not a known game action.'.format(action))

        things = tokens[1:]
        for t in things:
            if not t.lower() in self.game_things:
                raise errors.ParserError('The word {:s} not a known game thing.'.format(t))
        # Done.
        return action, things
