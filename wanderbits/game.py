#!/usr/bin/python

from __future__ import division, print_function, unicode_literals

import docopt

import executive


def main():
    """
    ---------------------------------------
    WanderBits: A text-based adventure game
    ---------------------------------------

    Usage:
        game.py [options]

    Options:
        -h --help      Show this help message.

    """

    # Parse command line arguments.
    args = docopt.docopt(main.__doc__)

    # Load data from config files.



    E = executive.Executive()

    # Start the event loop.
    E.run()

    print('Goodbye!')

    # Done.



if __name__ == '__main__':
    main()
