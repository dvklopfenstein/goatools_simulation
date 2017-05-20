"""Holds parameters used to create one set of experiments."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import timeit
import datetime


def get_hms(tic):
    """Print elapsed time as simulations run."""
    return str(datetime.timedelta(seconds=(timeit.default_timer()-tic)))


# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
