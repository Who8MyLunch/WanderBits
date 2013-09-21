
WanderBits Work Log
===================

This is a living document that will evolve as work progresses.

2013-09-21, 9:00 am
-------------------

I also need to include unit tests.  That will slow me down.  Might never get to the monster.

Write out an example game session.  Make sure to illustrate key types of actions and commands.  Think about a simple grammar for parsing user commands.  I could build a concise dictionary of verbs, nouns, maybe adjectives and adverbs, plus connector words.

Classes to define in-game objects, and how objects interact with each other and the user.

idea: start with class Thing from which all others inherit: items, rooms, and the user!

config file as a serialization of all in-game Things



2013-09-20, 8:30 pm
-------------------

Should there be a sense of time?  Would only make a difference if anything in the game had a temporal dependence.  Like another entity in the game!  A monster moving about could be neat, but it would also take time to implement.  Hmmm, maybe stuff like that should only be considered after the basic stuff is in place.  But still thinking along those lines: user has to search for a weapon while the monster is moving at random (or with a pattern?).  Very simple combat implemented as actions connecting weapons in possession with monster.  Some items might serve more damage than others.  The user and monster have finite amounts of hit points.  Turn-based attacks.  But if user waits too long, monster will go ahead and eat your head off.  Describe monster as horribly grotesque like Cthulhu.  I really like this Monster idea, but I must absolutely get the core features implemented first.  Monster is bonus fun stuff I get to do after the work part is done well.

The main objective here is to demonstrate my programming skills to SpaceX.  Tying in to fancy external libraries may not help me get further along here.  Some external libraries would certainly add nice features, but all that would do for me is demonstrate how well I can learn to use a foreign piece of software.  It is more important to write my own features from scratch, even though they will certainly not be as capable as something I might find somewhere online.  Forget about NLTK, forget about an AI bot, forget about a monster that will hunt down the user.

I can implement on my own all of the above required features.  It might be a boring game, but the instructions say nothing about making a fun game!  Ha!  Is that a loophole?  Maybe not. Nevermind. I will go crazy if I try to think or predict all the possible things they might be expecting.  I have to take the written instructions at face value.

Rooms are a connected graph.  I should take a look at the Graphviz DOT language?  http://www.graphviz.org/content/dot-language.  No, that's getting too complicated again.
