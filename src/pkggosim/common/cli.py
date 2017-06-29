"""Command-line interface."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys


def get_args():
    """Return a dictionary containing command-line arguments."""
    args = {
        'randomseed' : None, # A random seedn shall be generated
        'idx' : -1,
    }
    # Get arguments from command-line
    for arg in sys.argv[1:]:
        if arg.isdigit() or arg[:2] == "0x":
            args['randomseed'] = int(arg, 0)
        elif arg[:24] == "randomize_truenull_assc=":
            args['randomize_truenull_assc'] = arg[24:]
        elif arg[:2] == 'i=':
            args['idx'] = int(arg[2:])
    return args


# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.