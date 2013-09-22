
WanderBits Work Log
===================
This is a living document that will evolve as work progresses.

Saturday Evening
----------------
It's time to think about how to incorporate Unit Testing.  So far I have a `Parser`, an `Action`, and a `Thing`.  The `Parser` might be the simplest of the three.  Or at least right now I think I can visualize in my head all that it needs to do.   Hmmm, perhaps I should write down what those things are.  And then won't that set me up to write Unit Tests?  Curious.

  **Parser**: I could have some predefined sentences and confirm that the `Parser` parses them correctly.  This one seems straightforward enough.

  **Thing**: I described earlier some of the features that a basic `Thing` must have.  I could test the ability of putting something inside a `Thing` and then taking it back out.  Test whether a `Thing` inside of another `Thing` is visible or not.  Count how many items are inside.  Make more tests to cover new features of derived subclasses.

  **Action**: `Actions` make stuff happen.  A simple test would be to set up a game scenario and then make an `Action` do its thing.  Verify afterwards that the task got done.  That's all I can think of right now.  More later.


Saturday Afternoon
------------------
It feels like a slow start.  I have lots of ideas in my head and they are swirling and swirling.  I don't yet see clearly what the major components are going to be nor do I see how they will connect together.  I going to write next a few paragraphs describing the game.

### The Story

WanderBits is a game of adventure in the classic sense.  Remember Zork?  I sure do!  I remember learning about it in high school and being completely mesmerized by the entire concept.  It was like reading a book with which you could interact directly.  I could never get enough of those games!

The game of WanderBits is the story of a young man on a quest to explore his world.  We don't know the name of this person, or where he comes from.  The world he lives in right now is a bit of a puzzle.  It's made of up curiously-connected rooms, but some of the doors are locked and with no key in sight.  There must be a key somewhere around?  Maybe in that pot over there?  Maybe under the carpet?  Hmmm???  We must help this poor fellow find his way out of this game so he can continue on with his life!

Ok, I think that is enough for story time.

### Game Parts

Lets talk about a few important parts that make up the game engine.

  1. **Parser**: A text parsing system can be made as complicated as you can imaging.  The first thing I thought about was the Python-based Natural-Language Tool Kit (NLTK).  I've always been curious about it and I have wondered what kind of cools things I might do with it.  Shit!  Forget about that. Back on topic.

  A command parser for this type of game needs to support a relatively small number of basic functions.  It needs to know about actions for navigating and interacting with the game.  I needs to know about things to which the actions are directed.  A given command may involve multiple objects, e.g. put key in box.

  The scope of this task is such that I need to keep stuff simple.  Game commands will be defined by an action word plus one or more arguments.  It will be much simpler to implement if the number and kind of arguments for each command are static.

  Shit.  I just thought of something: does the command language also need to specified via config files?  I sure hope not...  Well, I just read the email again:

    > The game engine should be generic; as much as possible all the game specifics should live in the config file (description strings, supported verbs, room layout).

  It says _supported verbs_.  One way to interpret this is so: the game engine comes with predefined actions, the config file may specify which actions are available in a given game instance.  The config file could also specify any number of aliases for each aaction.  Another way to support this requirement is to write actual Python code in the config file that implements a particular action.  That would not meet the other requirement for the config file to be useable by a non-expert user.  I will assume for now that this interpretation is fine.

  Back on track.  Basic functionality of the `Parser` should be to receive as input text from the user after they presse the Enter key.  Idea: parse the text into a list of tokens using something basic like Python's shlex module.  Search from the start of the list for a word that matches the name of a command (including aliases).  Once found then begin second part of selecting the arguments.  White space is no problem.  But what about connector words like "the" or "a"?  e.g. "Take the apple" should be equivalent to "Take apple" and "Hey, take that apple" or "ehh, grab them apples".  I could maintain a list of ignore words and simply skip over them while parsing the user text for commands or arguments.  I like that idea a lot, but is it too simple??  I can also make aliases for the plural version of objects by adding an "s" to the end of each object's name.

  2. **Actions**: I really like the idea of having a fixed set of arguments for each action command.  I can define a base `Action` class that implements basic action capabilities.  Then create subclasses for each in-game action.  In order to perform its work, the `Action` instance will need access to local in-game items.  This could be done by searching through `Thing` instances, starting with the user `Thing`, and then other local `Things` for suitable matches to the argument list.

  An `Action` makes stuff happen by manipulating in-game `Things` represented by the input arguments.  An `Action` must be able to find the proper `Thing` instance(s) that are refered to by a given input argument.  These `Things` must be in the local area and also be visible, otherwise the action cannot take place.  For example, 'Take apple' may be interpreted as a task to be performed by an instance of `Take` (a subclass of `Action`).  `Take` could have a method such as `do_it()`, or `Take` itself may implement `__callable__` and thus be called directly with the input argument.  In this case, then input was the word 'apple'.  The `Take` action must be able to search the local area for an instance of `Thing` named 'apple'.  Once found, `Take` would first ask the apple `Thing` to remove itself from its current container.  Then the `Take` action would add the apple `Thing` to the user `Thing`'s container.

  3. **Things**: In-game content is to be represented by objects subclassed from a `Thing` base class.  Items like an apple or a key could be represented by a `Thing`.  But it gets better.  A room could be a `Thing`, and even the user could be a `Thing`.  A `Thing`-based object would know about concepts such as what other `Thing` is it inside of?  A room, a box, or the user's pocket?  The act of moving the user from one room to another would involve moving the user `Thing` over to the inside of the next room `Thing`.  The basic `Thing` class should handle stuff being inside of other stuff.  This means a `Thing` must know about the sizes of `Things` and the size of its own insides.  A `Thing` can be destroyed.  The set of `Things` inside a `Thing` may or may not be visible to the nearby user.  This allows for a box to be opened or closed.  Only `Things` that are visible may serve as valid `Action` arguments.  A `Thing` is able to describe its appearance when the user looks at it.

  4. **Executive**:  All the stuff above needs to be attached to something and somewhere there needs to be an event loop running around.  Right now I'm thinking there could be an `Executive` module that is the central place where everything comes together.  It might be a simple module with a bunch of functions, or maybe it should be its own Class, perhaps yet another kind of `Thing`?  This executive could also be responsible for reading text from the user, and then also printing responses back to the user.

Saturday Morning
----------------
I also need to include unit tests.  That will slow me down.  Might never get to the monster :(

Write out an example game session.  Make sure to illustrate key types of actions and commands.  Think about a simple grammar for parsing user commands.  I could build a concise dictionary of verbs, nouns, maybe adjectives and adverbs, plus connector words.

Classes to define in-game objects, and how objects interact with each other and the user.  Idea: start with class Thing from which all others inherit: items, rooms, and the user!  The config file as a serialization of all in-game Things.

Friday Evening
--------------
I received the technical test from SpaceX this afternoon.  Wooo!

Should there be a sense of time?  Would only make a difference if anything in the game had a temporal dependence.  Like another entity in the game!  A monster moving about could be neat, but it would also take time to implement.  Hmmm, maybe stuff like that should only be considered after the basic stuff is in place.  But still thinking along those lines: user has to search for a weapon while the monster is moving at random (or with a pattern?).  Very simple combat implemented as actions connecting weapons in possession with monster.  Some items might serve more damage than others.  The user and monster have finite amounts of hit points.  Turn-based attacks.  But if user waits too long, monster will go ahead and eat your head off.  Describe monster as horribly grotesque like Cthulhu.  I really like this Monster idea, but I must absolutely get the core features implemented first.  Monster is bonus fun stuff I get to do after the work part is done well.

The main objective here is to demonstrate my programming skills to SpaceX.  Tying in to fancy external libraries may not help me get further along here.  Some external libraries would certainly add nice features, but all that would do for me is demonstrate how well I can learn to use a foreign piece of software.  It is more important to write my own features from scratch, even though they will certainly not be as capable as something I might find somewhere online.  Forget about NLTK, forget about an AI bot, forget about a monster that will hunt down the user.

I can implement on my own all of the above required features.  It might be a boring game, but the instructions say nothing about making a fun game!  Ha!  Is that a loophole?  Maybe not. Nevermind. I will go crazy if I try to think or predict all the possible things they might be expecting.  I have to take the written instructions at face value.

Rooms are a connected graph.  I should take a look at the Graphviz DOT language?  http://www.graphviz.org/content/dot-language.  No, that's getting too complicated again.
