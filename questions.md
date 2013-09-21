
Questions and Answers
=====================

**Question 1**: Shit.  I just thought of something: does the command language also need to specified via config files?  I sure hope not...  Well, I just read the email again:

  > The game engine should be generic; as much as possible all the game specifics should live in the config file (description strings, supported verbs, room layout).

It says "__supported verbs__".  One way to interpret this is so: the game engine comes with predefined actions, the config file may specify which actions are available in a given game instance.  The config file could also specify any number of aliases for each aaction.  Another way to support this requirement is to write actual Python code in the config file that implements a particular action.  That would not meet the other requirement for the config file to be useable by a non-expert user.

Is this a fair interpretation of the rules?



