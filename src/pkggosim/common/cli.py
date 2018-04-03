"""Command-line interface."""

__copyright__ = "Copyright (C) 2016-2018, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import sys


def get_args():
    """Return a dictionary containing command-line arguments."""
    args = {
        'title': None,
        'genes': [4, 16, 64, 128],
        'randomseed' : None, # A random seed shall be generated
        'randomize_truenull_assc' : 'orig_noprune_ntn2',
        'idx_experiment_cnts' : -1,
        'idx_max_sigpvals' : 0,
        'propagate_counts': False,
    }
    # Get arguments from command-line
    for arg in sys.argv[1:]:
        if arg.isdigit() or arg[:2] == "0x":
            args['randomseed'] = int(arg, 0)
        elif arg[:6] == "genes=":
            args['genes'] = [int(n) for n in arg[6:].split(',')]
        elif arg[:6] == "title=":
            args['title'] = arg[6:]
        elif arg[:24] == "randomize_truenull_assc=":
            args['randomize_truenull_assc'] = arg[24:]
        elif arg[:9] == "propcnts=":
            if arg[9] == "T":
                args['propagate_counts'] = True
        elif arg[:2] == 'e=':
            args['idx_experiment_cnts'] = int(arg[2:])
        elif arg[:2] == 'p=':
            args['idx_max_sigpvals'] = int(arg[2:])
    sys.stdout.write("ARGS: {ARGS}\n".format(ARGS=args))
    return args


# Copyright (C) 2016-2018, DV Klopfenstein, Haibao Tang. All rights reserved.
