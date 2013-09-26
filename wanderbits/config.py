#!/usr/bin/python

from __future__ import division, print_function, unicode_literals

"""
Read and write game config files.
"""

import yaml


def read(fname):
    """
    Read game config information from file.
    """
    info = yaml.load(open(fname))
    return info


def write(fname, info):
    """
    Write game config information to file.
    """
    with open(fname, 'w') as fo:
        yaml.safe_dump(info, stream=fo, width=50,
                       indent=4, default_flow_style=False)
