#!/usr/bin/python

from __future__ import division, print_function, unicode_literals

"""
Executive class for WanderBits, a text-based adventure game.
"""

import sys

import errors
import line_parser
import things
import actions as actions_module   # too confusing keeping original name!


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

        self.verbose = verbose

        # Storage for game content.
        self._user = None
        self._rooms = []
        self._items = []
        self._actions = []

        # Ingest game config information.
        if isinstance(game_info, dict):
            self.ingest_config(game_info)

        elif isinstance(game_info, list):
            for g in game_info:
                self.ingest_config(g)

        else:
            msg = 'Invalid game_info: {:s}'.format(str(type(game_info)))
            raise errors.ExecutiveError(msg)

        # Build parser with valid action names.
        action_names = []
        for a in self.actions:
            action_names += a.names
        self.parser = line_parser.Parser(action_names, verbose=self.verbose)

        # Setup stdin and stdout.
        if stdin:
            self.stdin = stdin
        else:
            self.stdin = sys.stdin

        if stdout:
            self.stdout = stdout
        else:
            self.stdout = sys.stdout

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        if isinstance(value, things.User):
            self._user = value
        else:
            msg = 'Input value must be a user: {:s}'.format(str(value))
            raise errors.ExecutiveError(msg)

    @property
    def actions(self):
        """
        List of known in-game actions.
        """
        return self._actions

    @actions.setter
    def actions(self, value):
        if isinstance(value, actions_module.Action):
            self._actions.append(value)
        else:
            msg = 'Input value must be an Action: {:s}'.format(str(value))
            raise errors.ActionError(msg)

    def ingest_config(self, game_info):
        """
        Take in config dicts and instantiate in-game Things and Actions.
        This function may be called multiple time in order to ingest multiple
        config files.
        """
        # Create game rooms.
        for info in game_info['rooms']:
            room = things.Room(verbose=self.verbose, **info)
            self._rooms.append(room)

            if self.verbose:
                print('room: {:s}, {:s}'.format(room.name, room.description))

        # Create game items.
        for info in game_info['items']:
            item = things.Item(verbose=self.verbose, **info)

            # Place item in a room.
            room_start = things.find_thing(self._rooms, info['start'])
            room_start.add(item)

            self._items.append(item)

            if self.verbose:
                print('item: {:s}, {:s}'.format(item.name, item.description))

        # Create user object(s).
        for info in game_info['user']:
            self.user = things.User(verbose=self.verbose, **info)

            # Place user in a room.
            room_start = things.find_thing(self._rooms, info['start'])
            room_start.add(self.user)

            if self.verbose:
                print('user: {:s}, {:s}'.format(self.user.name,
                                                self.user.description))

        # Create game actions.
        for action_info in game_info['actions']:
            # Get action sub-class from actions module.
            name = action_info['name'].lower().title()
            action_class = getattr(actions_module, name)

            # Instantiate Action class.
            action = action_class(self.user,  action_info['description'],
                                  action_info['aliases'])
            self.actions.append(action)

            if self.verbose:
                print('action: {:s}, {:s}'.format(action.names,
                      action.description))

    #############################################
    # Input and output to user console.
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
        while True:
            try:
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
    # Running the game.
    def find_action(self, user_action_name):
        """
        Return Action sub-class instance that matches user's action name.
        """
        # Loop over known game actions.
        for action in self.actions:
            # Does it match?
            if user_action_name in action.names:
                return action

        # No match found.
        msg = 'Not a valid action: {:s}'.format(user_action_name)
        raise errors.ExecutiveError(msg)

    def start(self):
        """
        Start running the Executive's event loop.  Block until user's game
        session is finished.
        """
        try:
            # Main loop.
            self.console_write('\nWelcome\n')
            for line in self.console_reader():
                try:
                    # Parse new line of text.
                    user_action_name, user_arguments = self.parser.parse(line)

                    # Take action!
                    game_action = self.find_action(user_action_name)
                    response = game_action.apply(*user_arguments)

                # Catch some easy errors inside the event loop.
                except errors.ParserError as e:
                    # catch when user supplied word is not a valid action.
                    response = e.message

                # Send response to user.
                self.console_write(response)

        # Catch difficult errors outside the event loop.
        # I am not happy with all these 'return' statements below.  This
        # should really be more elegant.
        except errors.NiceExitError as e:
            self.console_write('Exit!')

        except errors.FatalError as e:
            self.console_write('Fatal game error: {:s}'.format(e.message))
            return

        except errors.GameError as e:
            msg = 'Unhandled game error: {:s}, {:s}'.format(type(e), e.message)
            self.console_write(msg)
            return

        except Exception as e:
            msg = 'unhandled Python exception: {:s}'.format(e.message)
            self.console_write(msg)
            return

        self.console_write('Saving game state...')

        # Save game state.
        # TODO: save game info.

        # Hello! Goodbye!
        self.console_write('Bye.\n')


if __name__ == '__main__':
    pass
