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
    def apply(self, user, *args):
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

    def apply(self, user, *args):
        """
        Make the character go somewhere.
        """
        print('apply')
        for a in args:
            print(a)

        return 'measfdasfda'


class Look(Action):

    def __init__(self, description=None, aliases=[]):
        """
        Introspection of nearby items.
        """
        self._names = ['look'] + aliases
        self._description = description

    def apply(self, user, *args):
        """
        Look at something nearby.
        Take first argument as action target.
        Default to looking at current room if no args supplied.
        """
        if not args:
            # Default to look at the room.
            args = ['room']
l
        target = args[0]
        # Find Things at which to look, assuming target is name of a thing

        print('apply')
        for a in args:
            print(a)

        return 'measfdasfda'


class Take(Action):

    def __init__(self, description=None, aliases=[]):
        """
        Acquire a nearby item.
        """
        self._names = ['take'] + aliases
        self._description = description

    def apply(self, user, *args):
        """
        Acquire something from local scope.
        """
        print('apply')
        for a in args:
            print(a)

        return 'measfdasfda'


class Put(Action):

    def __init__(self, description=None, aliases=[]):
        """
        Acquire a nearby item.
        """
        self._names = ['put'] + aliases
        self._description = description

    def apply(self, user, *args):
        """
        Acquire something from local scope.
        """
        print('apply')
        for a in args:
            print(a)

        return 'measfdasfda'


class Quit(Action):

    def __init__(self, description=None, aliases=[]):
        """
        End the game.
        """
        self._names = ['quit'] + aliases
        self._description = description

    def apply(self, user, *args):
        """
        Acquire something from local scope.
        """
        print('apply')
        for a in args:
            print(a)

        return 'measfdasfda'


if __name__ == '__main__':
    A = Go(['asd'])
