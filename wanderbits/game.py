#!/usr/bin/python

from __future__ import division, print_function, unicode_literals

import argparse
import executive
import config


def main():
    """
    ---------------------------------------
    WanderBits: A text-based adventure game
    ---------------------------------------
    """

    description = 'WanderBits: a text-based adventure game!'
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('--restore', default=None,
                        help='previously-saved game file.')

    parser.add_argument('--config', default='game.yml',
                        help='game configuration file.')

    # Parse command line arguments.
    args = parser.parse_args()

    # Load data from config files.
    fname_restore = args.config
    info = config.read(fname_restore)

    # Start the game.
    E = executive.Executive(options=info)
    E.start()

    # Done.


if __name__ == '__main__':
    main()
