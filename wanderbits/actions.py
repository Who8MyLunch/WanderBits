#!/usr/bin/python

from __future__ import division, print_function, unicode_literals

"""
Action class for WanderBits, a text-based adventure game.
"""

import abc
# import errors


__all__ = ['Go', 'Look', 'Take', 'Quit']


class Action(object):
    """
    Action class for WanderBits, a text-based adventure game.
    This class is a base class.  Inherit from this class to implement a
    particular game action.
    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self):
        """
        Initialize Action class.

        Aliases allow for user-defined custom action names.
        Each game action needs to be implemented as a subclass of the Action
        base class.
        """
        pass

    @property
    def names(self):
        """
        List of this Action's characteristic names, inclkuding any aliases
        """
        return self._names

    @property
    def description(self):
        """
        This Action's description.
        """
        return self._description

    @abc.abstractmethod
    def apply(self, *args):
        """
        Do the work required for this action.
        Each game action needs to be implemented as a subclass of the Action
        base class.
        """
        pass

#################################################


class Go(Action):

    def __init__(self, description=None, aliases=[]):
        """
        Character navigation action.
        """
        self._names = ['go'] + aliases
        self._description = description

    def apply(self, *args):
        """
        Make the character go somewhere.
        """
        print('apply')
        for a in args:
            print(a)


class Look(Action):

    def __init__(self, description=None, aliases=[]):
        """
        Introspection of nearby items.
        """
        self._names = ['look'] + aliases
        self._description = description

    def apply(self, *args):
        """
        Look at something nearby.
        """
        print('apply')
        for a in args:
            print(a)


class Take(Action):

    def __init__(self, description=None, aliases=[]):
        """
        Acquire a nearby item.
        """
        self._names = ['take'] + aliases
        self._description = description

    def apply(self, *args):
        """
        Acquire something from local scope.
        """
        print('apply')
        for a in args:
            print(a)


class Put(Action):

    def __init__(self, description=None, aliases=[]):
        """
        Acquire a nearby item.
        """
        self._names = ['put'] + aliases
        self._description = description

    def apply(self, *args):
        """
        Acquire something from local scope.
        """
        print('apply')
        for a in args:
            print(a)


class Quit(Action):

    def __init__(self, description=None, aliases=[]):
        """
        End the game.
        """
        self._names = ['quit'] + aliases
        self._description = description

    def apply(self, *args):
        """
        Acquire something from local scope.
        """
        print('apply')
        for a in args:
            print(a)


if __name__ == '__main__':
    A = Go(['asd'])
