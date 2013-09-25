
WanderBits To Do List
=====================

Near-Term Tasks
---------------
- Undo Console, move its functionality over to Executive
- Think about how everything plugs into the Executive module.
- Hook up Parser to Executive
- Unit test for Executive.
- Write the basic Thing class
- Write the basic Action class


Long Term
---------
- Define layout for testing rooms
- Define a few simple items
- Serialize Things, Actions to YAML file.  Basis for defining game via config files.
- Think about saving game progress.  serialize all stuff into a zip file.


Research Topics
---------------
- Need a source of words for room descriptions, item descriptions.  Response to actions, e.g. moving, taking, dropping...
- ???? more to come.
- How to handle door locks and keys??


Finished Tasks
--------------
- Hook up Console to Executive
- Update Console class to provide a command prompt.  Manage line spacing between user input text and game response text.
- Write the basic Executive module
- Run a simple event loop
- Think about sys.stdin, sys.stdout to manage IO with user, tied to Console class.
- Think about basic Console class
- Write basic unit tests for Parser class
- Write the basic Parser class
- Command parsing system, nouns, verbs, subjects, objects.  still not very clear about this
- Think about an Errors class.
- Think about what unit tests could be used to ensure proper operation of each functional element.
- Write overview application description.  A paragraph or two, perhaps describing the user experience.
- Describe the critical functional elements that make the application work.
- Define approximate order for writing core features
