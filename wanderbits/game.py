#!/usr/bin/python

from __future__ import division, print_function, unicode_literals

import argparse
import executive
import config
import errors


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

    parser.add_argument('--verbose', default=False, action='store_true',
                        help='display information while running.')

    # Parse command line arguments.
    args = parser.parse_args()

    # Load data from config files.
    try:
        game_info = config.read(args.config)
    except IOError as e:
        print(e.message)
        return

    # Start the game.
    try:
        E = executive.Executive(game_info, verbose=args.verbose)
        E.start()
    except errors.GameError as e:
        print(e.message)

    # Done.


if __name__ == '__main__':
    main()
