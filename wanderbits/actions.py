#!/usr/bin/python

from __future__ import division, print_function, unicode_literals

"""
Action class for WanderBits, a text-based adventure game.
"""

import abc
import errors
import things

__all__ = ['Go', 'Look', 'Take', 'Put', 'Help', 'Quit']


def find_action(many_actions, name):
    """
    Find a matching Action by name.
    """
    if not isinstance(name, basestring):
        msg = 'name must be a string: {:s}'.format(str(name))
        raise errors.ActionError(msg)

    for a in many_actions:
        if name in a.names:
            return a

    msg = 'Unable to find matching Thing: {:s}'.format(name)
    raise errors.FindActionError(msg)

#################################################


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
        self._user = None

    @property
    def names(self):
        """
        List of this Action's characteristic names, inclkuding any aliases
        """
        return self._names

    @property
    def user(self):
        """
        Game User instance.
        """
        return self._user

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

    def __init__(self, user, description=None, aliases=[]):
        """
        Character navigation action.
        """
        self._user = user
        self._names = ['go'] + aliases
        self._description = description

    def apply(self, *args):
        """
        Make the character go somewhere.
        """
        print('apply')
        for a in args:
            print(a)

        return 'measfdasfda'


class Look(Action):

    def __init__(self, user, description=None, aliases=[]):
        """
        Introspection of nearby items.
        """
        self._user = user
        self._names = ['look'] + aliases
        self._description = description

    def apply(self, *args):
        """
        Look at something nearby.
        Take first argument as action target.
        Default to looking at current room if no args supplied.
        """
        if not args:
            # Default to look at the room.
            args = ['room']

        # Find Things at which to look, assuming argument is name of a thing.
        target = args[0]
        try:
            # Search through user-local things by name.
            target_thing = things.find_thing(self.user.local_things, target)
        except errors.FindThingError:
            pass

        print('apply')
        print(target_thing)
        for a in args:
            print(a)

        return 'measfdasfda'


class Take(Action):

    def __init__(self, user, description=None, aliases=[]):
        """
        Acquire a nearby item.
        """
        self._user = user
        self._names = ['take'] + aliases
        self._description = description

    def apply(self, *args):
        """
        Acquire something from local scope.
        """
        print('apply')
        for a in args:
            print(a)

        return 'measfdasfda'


class Put(Action):

    def __init__(self, user, description=None, aliases=[]):
        """
        Acquire a nearby item.
        """
        self._user = user
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


class Help(Action):

    def __init__(self, user, description=None, aliases=[]):
        """
        Give advice on how to play the game.
        """
        if not description:
            description = self.__doc__

        self._user = user
        self._names = ['help'] + aliases
        self._description = description

    def apply(self, *args):
        return self.description


class Quit(Action):

    def __init__(self, user, description=None, aliases=[]):
        """
        End the game.
        """
        self._user = user
        self._names = ['quit'] + aliases
        self._description = description

    def apply(self, *args):
        """
        Raise error signalling time to exit the game in an orderly fashion.
        """
        raise errors.NiceExitError('Exit the game nicely.')


if __name__ == '__main__':
    pass
