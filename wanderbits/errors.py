#!/usr/bin/python

"""
Exceptions for the game WanderBits.
"""


class GameError(Exception):
    pass


class ParserError(GameError):
    pass


class ExecutiveError(GameError):
    pass


class ActionError(GameError):
    pass


class ThingError(GameError):
    pass


class ConsoleError(GameError):
    pass



