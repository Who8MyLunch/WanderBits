WanderBits
==========

A simple text-based adventured game.

Goal
----

Demonstrate software design skills


Objectives
----------

 - Create a text-based interactive adventure game
 - Create a generic game engine
 - Define game content using config file(s)
   - Config files must be simple enough to enable the casual user to create new content
 - Game world must consist of multiple rooms
 - User able to issue simple multi-word commands at prompt
   - navigation, e.g. go north
   - introspection, e.g. inspect room
   - action, e.g. pick up crowbar
   - help, e.g. help go




The main objective here is to demonstrate my programming skills to SpaceX.  Tying in to fancy external libraries may not help me get further along here.  Some external libraries would certainly add capability, but all that would for me is demonstrate how well I can learn to use a foreign piece of software.  It is more important to write my own features from scratch, even though they will certainly not be as capable as something I might find somewhere online.  Forget about NLTK, forget about AI bot.



Some Thoughts
-------------

I can implement on my own all of the above features.  It might be a boring game, but the instructions say nothing about making a fun game!  Ha!  Is that a loophole?  Maybe not.  As part of implementing the above core features, I would write quite a bit of code, using multiple modules and classes.

Should there be a sense of time?  Would only make a difference if anything in the game had a temporal dependence.  Like another entity in the game!  A monster moving about could be neat, but it would also take time to implement.  Hmmm, maybe stuff like that should only be considered after the basic stuff is in place.  But still thinking along those lines: user has to search for a weapon while the monster is moving at random (or with a pattern?).  Very simple combat implemented as actions connecting weapons in possession with monster.  Some items might serve more damage than others.  The user and monster have finite amounts of hit points.  Turn-based attacks.  But if user waits too long, monster will go ahead and eat your head off.  Describe monster as horribly grotesque like Cthulhu.  I really like this Monster idea, but I must absolutely get the core features implemented first.  Monster is bonus fun stuff I get to do after the work part is done well.

Rooms are a connected graph.  I should take a look at the Graphviz DOT language?  http://www.graphviz.org/content/dot-language.

I also need to include unit tests.  That will slow me down.  Might never get to the monster.

Write out an example game session.  Make sure to illustrate key types of actions and commands.  Think about a simple grammar for parsing user commands.  I could build a concise dictionary of verbs, nouns, maybe adjectives and adverbs, plus connector words.

Near-Term Tasks
---------------

    - Write overview application description.  A paragraph or two, perhaps describing the user experience.
    - Describe the critical functional elements that make the application work.
    - Think about what unit tests could be used to ensure proper operation of each functional element.

Long

Research
--------

Do some research on software approaches for parts that are still not clear:

    - User command prompt and console.  read user text, display response.
    - Command parsing system, nouns, verbs, subjects, objects.  still not very clear about this
    - Need a source of words for room descriptions, item descriptions.  Response to actions, e.g. moving, taking, dropping...
    - ???? more to come.


-----

    Classes to define in-game objects, and how objects interact with each other and the user.
 - idea: start with class Thing from which all others inherit: items, rooms, and the user!

config file as a serialization of all in-game Things
