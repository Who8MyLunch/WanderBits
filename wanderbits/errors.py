#!/usr/bin/python

from __future__ import division, print_function, unicode_literals

"""
Exceptions for the game WanderBits.
"""


class GameError(Exception):
    pass


class ConsoleError(GameError):
    pass


class ParserError(GameError):
    pass


class ExecutiveError(GameError):
    pass


class ActionError(GameError):
    pass


class ThingError(GameError):
    pass
