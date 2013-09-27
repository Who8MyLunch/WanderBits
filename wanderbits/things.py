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
    Find a matching Thing.
    """
    for t in many_things:
        if t.name == name:
            return t

    raise errors.ThingError('Unable to find matching Thing: {:s}'.format(name))

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

        # Other game Things will occupy this Thing's various scopes
        self._scope_0 = []  # intimate
        self._scope_1 = []  # local
        self._scope_2 = []  # global

        # Which Thing contains the current Thing.
        self._parent = None

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

    def add(self, obj):
        """
        Place an object inside oneself.
        """
        self._container.add(obj)

    def remove(self, obj):
        """
        Remove an object from oneself.
        """
        self._container.pop(obj)

#################################################
#################################################

# nice discussion that clarifies inheriting from an
# abstract class and using super()
# http://pymotw.com/2/abc/#concrete-methods-in-abcs


class Room(Thing):
    """
    Room object.
    """
    property_keys = ['connections']

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
    property_keys = ['capacity']

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.update_properties(self.property_keys, kwargs)

#################################################


if __name__ == '__main__':
    """
    Examples and ideas.
    """

    info = {'name': 'closet',
            'description': 'sdfsdfsdfsdfdsfdsf',
            'size': 1000,
            'capacity': 10,
            'connections': {'west': 'den',
                            'east': 'livingroom'}
            }

    r = Room(**info)
