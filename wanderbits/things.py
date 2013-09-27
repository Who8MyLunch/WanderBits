#!/usr/bin/python

from __future__ import division, print_function, unicode_literals

"""
Things class for WanderBits, a text-based adventure game.
"""

import abc
import errors


# Helpers
def find_thing(many_things, name):
    """
    Find a matching Thing by name.
    """
    if not isinstance(name, basestring):
        msg = 'name must be a string: {:s}'.format(str(name))
        raise errors.ThingError(msg)

    for t in many_things:
        if t.name == name:
            return t

    msg = 'Unable to find matching Thing: {:s}'.format(name)
    raise errors.FindThingError(msg)

#################################################


class Thing(object):
    """
    Things class for WanderBits, a text-based adventure game.
    This class is a base class.  Inherit from this class to implement
    a particular game item.
    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, **kwargs):
        """
        Initialize Thing class.
        Each kind of game item needs to be implemented as a subclass of
        the Thing base class.
        """
        base_property_keys = ['name', 'description']

        self._properties = {}
        self.update_properties(base_property_keys, kwargs)

        # Things are able to contain other Things.
        self._container = []

        # Which Thing contains the current Thing.
        self._parent = None

    def __repr__(self):
        return 'Thing [{:s}]'.format(self.name)

    def update_properties(self, property_keys, mapping):
        """
        Update this Thing's inherent property values.
        """
        for k in property_keys:
            try:
                self._properties[k] = mapping[k]

            except KeyError:
                print(k)
                raise

    @property
    def name(self):
        """
        This Thing's characteristic name.
        """
        return self._properties['name']

    @property
    def description(self):
        """
        This Thing's description.
        """
        return self._properties['description']

    @property
    def size(self):
        """
        This Thing's physical size.
        """
        try:
            return self._properties['size']
        except KeyError:
            return 0
            # msg = 'Thing hasn't a size: {:s}'.format(self.name)
            # raise errors.ThingError(msg)

    @property
    def capacity(self):
        """
        This Thing's physical size.
        """
        try:
            return self._properties['capacity']
        except KeyError:
            return 0
            # msg = 'Thing hasn't a capacity: {:s}'.format(self.name)
            # raise errors.ThingError(msg)

    @property
    def parent(self):
        """
        Another Thing that contains self.
        """
        return self._parent

    @parent.setter
    def parent(self, value):
        if isinstance(value, Thing) or value is None:
            # TODO: I don't like having None here as a valid input.
            self._parent = value
        else:
            msg = 'Parent must be a Thing: {:s}'.format(str(value))
            raise errors.ThingError(msg)

    def add(self, obj):
        """
        Place new object inside oneself.
        """
        if not isinstance(obj, Thing):
            msg = 'Object must be a Thing: {:s}'.format(str(obj))
            raise errors.ThingError(msg)

        if obj in self._container:
            msg = '{:s} already contains {:s}'.format(self, obj)
            raise errors.ThingError(msg)

        if self.available_space < obj.size:
            msg = 'Not enough room in {:s} to contain {:s}'.format(self, obj)
            raise errors.ThingError(msg)

        # Add to container, update it's parent.
        self._container.append(obj)
        obj.parent = self

    def remove(self, obj):
        """
        Remove object from oneself.
        """
        try:
            # Remove from container, remove self as parent.

            self._container.remove(obj)
            obj.parent = None

        except ValueError:
            msg = '{:s} does not contains {:s}'.format(self, obj)
            raise errors.ThingError(msg)

    @property
    def container(self):
        """
        A list of Things contained by this Thing.
        """
        return self._container

    @property
    def available_space(self):
        """
        Amount of space inside this Thing available for storing more Things.
        """
        contained_size = 0
        for T in self._container:
            contained_size += T.size
        return self.capacity - contained_size

#################################################
#################################################

# nice discussion that clarifies inheriting from an abstract class and
# using also using super():
# http://pymotw.com/2/abc/#concrete-methods-in-abcs


class Room(Thing):
    """
    Room object.
    """
    property_keys = ['connections', 'size', 'capacity']

    def __init__(self, **kwargs):
        super(Room, self).__init__(**kwargs)
        self.update_properties(self.property_keys, kwargs)

    @property
    def connections(self):
        """
        Mapping to other rooms.
        """
        return self._properties['connections']

#################################################


class Item(Thing):
    """
    Item object.
    """
    property_keys = ['size', 'capacity']

    def __init__(self, **kwargs):
        super(Item, self).__init__(**kwargs)
        self.update_properties(self.property_keys, kwargs)

#################################################


class User(Thing):
    """
    User object.
    """
    property_keys = ['size', 'capacity']

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.update_properties(self.property_keys, kwargs)

    @property
    def local_things(self):
        """
        Return list of Things that are nearby.
        These are Things that may be either physically manipulated or observed.
        This includes the current room, Things in the room, Things held
        by the user.  Does not include Things inside Things held
        by the user.
        """
        # User should be contained by a room.
        room = self.parent

        # List of things.
        things = [room] + room.container + self.container

        # Remove self from list.
        things.remove(self)

        return things

#################################################


if __name__ == '__main__':
    pass
