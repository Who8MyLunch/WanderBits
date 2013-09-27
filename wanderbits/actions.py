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

        # TODO: get room object, verify target direction is valid, remove user
        # from current room, add to target room, issue Look command.


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
        Accept a string name or an Item instance.
        Default to looking at current room if no args supplied.
        """
        if not args:
            # Default is to look at the room the user is inside.
            args = [self.user.parent.name]

        # Consider first argument as target for looking.
        target = args[0]
        if isinstance(target, things.Item):
            thing_targ = target
        elif isinstance(target, basestring):
            # Search local area for Item with matching name.
            try:
                thing_targ = things.find_thing(self.user.local_things, target)
            except errors.FindThingError:
                msg = "There isn't a '{:s}' nearby ".format(target)
                raise errors.ApplyActionError(msg)
        else:
            msg = "I don't know what to do with: {:s}".format(target)
            raise errors.ApplyActionError(msg)

        # Gather up Items that inside the target Thing.
        response = 'You see {:s}.'.format(thing_targ.description)

        # Build up nice string of the extra stuff also found here.
        extra = None
        num_inside = len(thing_targ.container)
        if num_inside > 2:
            names = [t.name for t in thing_targ.container[:-1]]
            extra = ', '.join(names) + ' and ' + thing_targ.container[-1].name
        elif num_inside == 2:
            n1 = thing_targ.container[0].name
            n2 = thing_targ.container[1].name
            extra = n1 + ' and ' + n2

        elif num_inside == 1:
            extra = thing_targ.container[0].name

        if extra:
            response += '\nThe room also contains ' + extra + '.'

        return response


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

        # TODO: search for item, try to add to user's container.  if error
        # message back that can't get that thing.

        if args:
            response = 'You try as best you can to pick up "{:s}", but ' + \
                       'alas your muscles have atrophied due to lack of ' + \
                       'excersise on your last trip to Outer Space.'
            response = response.format(args[0])

        else:
            response = 'Take what?!  What do you mean?'

        return response


class Put(Action):

    def __init__(self, user, description=None, aliases=[]):
        """
        Acquire a nearby item.
        """
        self._user = user
        self._names = ['put'] + aliases
        self._description = description

    def apply(self, *args):
        """
        Acquire something from local scope.
        """

        # TODO: verify target item is in our possession, remove from user,
        # add to room.

        response = 'That seems like a lot of work.  Please try again.'

        return response

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
