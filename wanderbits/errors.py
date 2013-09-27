#!/usr/bin/python

from __future__ import division, print_function, unicode_literals

"""
Exceptions for the game WanderBits.
"""


class GameError(Exception):
    pass


class ConfigError(GameError):
    pass


class ThingError(GameError):
    pass


class FindThingError(ThingError):
    pass


class ActionError(GameError):
    pass


class FindActionError(ActionError):
    pass


class LookActionError(ActionError):
    pass


class ParserError(GameError):
    pass


class ExecutiveError(GameError):
    pass


class NiceExitError(GameError):
    pass


class FatalError(GameError):
    pass
