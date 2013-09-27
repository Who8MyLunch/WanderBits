#!/usr/bin/python

from __future__ import division, print_function, unicode_literals

"""
Executive class for WanderBits, a text-based adventure game.
"""

import sys

import errors
import line_parser
import things
import action


class Executive(object):
    """
    Executive class for WanderBits, a text-based adventure game.
    """

    def __init__(self, game_info, stdin=None, stdout=None, verbose=False):
        """
        Initialize Executive class instance.

        game_info: a dict or a sequence of dicts containing game configuration
        information.

        stdin, stdout: default to sys.stdin and sys.stdout
        """

        # Storage for game content.
        self._rooms = []
        self._items = []
        self._actions = []

        # Ingest game config information.
        if isinstance(game_info, dict):
            self.ingest_config(game_info, verbose=verbose)

        elif isinstance(game_info, list):
            for g in game_info:
                self.ingest_config(g, verbose=verbose)

        else:
            msg = 'Invalid game_info: {:s}'.format(str(type(game_info)))
            raise errors.ExecutiveError(msg)

        # Setup stdin and stdout.
        if stdin:
            self.stdin = stdin
        else:
            self.stdin = sys.stdin

        if stdout:
            self.stdout = stdout
        else:
            self.stdout = sys.stdout

        actions = ['go', 'quit', 'exit']
        self.parser = line_parser.Parser(actions)

    def ingest_config(self, game_info, verbose=False):
        """
        Take in config dicts and instantiate in-game Things and Actions.
        This function may be called multiple time in order to ingest multiple
        config files.
        """
        # Create game rooms.
        for a in game_info['rooms']:
            room = things.Room(verbose=verbose, **a)
            self._rooms.append(room)

            if verbose:
                print('room: {:s}, {:s}'.format(room.name, room.description))

        # Create game items.
        for a in game_info['items']:
            item = things.Item(verbose=verbose, **a)
            self._items.append(item)

            if verbose:
                print('item: {:s}'.format(item.name))

        # Create game actions.
        for name, aliases in game_info['action_aliases'].items():
            # Get action sub-class from action module.
            Action_obj = getattr(action, name.lower().title())

            # Instantiate Action class.
            instance = Action_obj(aliases)
            self._actions.append(instance)

            if verbose:
                print('alias: {:s}'.format(instance.names))

    #############################################
    # Console read/write
    def console_read(self):
        """
        Read a line of text from the user.  Block until user hits enter.
        Also handle nice display of command prompt.
        """
        self.stdout.write('\n> ')
        line = self.stdin.readline()

        return line.strip()

    def console_reader(self):
        """
        A generator to yield user's lines of text to the caller.
        """
        try:
            while True:
                yield self.console_read()

        except KeyboardInterrupt:
            # catch when the user hits ctrl-c at the prompt.
            # Yield exit command.  This is just as if the user had
            # typed this at the game prompt.
            yield 'exit'

    def console_write(self, text):
        """
        Write some text out to the user.
        """
        output = '{:s}\n'.format(text)
        self.stdout.write(output)

    #############################################

    def start(self):
        """
        Start running the Executive's event loop.  Block until user's game
        session is finished.
        """
        try:
            # Main loop.
            self.console_write('\nWelcome\n')
            for line in self.console_reader():

                # Parse new line of text.
                action_name, arguments = self.parser.parse(line)

                # Take action!

                # Send response to user.
                response = 'hello!!!! ' + action_name
                self.console_write(response)

        except errors.GameError as e:
            print(e)
            raise

        self.console_write('Exit!\nSaving game state...')

        # Save game state.
        # TODO: save game info.

        # End the game nicely.
        self.console_write('Bye.\n')


if __name__ == '__main__':
    pass
