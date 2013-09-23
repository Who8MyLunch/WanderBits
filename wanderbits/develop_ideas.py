#!/usr/bin/python

"""
Test and develop game ideas here.
"""

import sys



import errors
import line_parser


# Setup.
known_actions = ['go', 'look', 'help']

P = line_parser.Parser()

line = 'put the chair in the box'

print(P.parse(line))


# Do it.
