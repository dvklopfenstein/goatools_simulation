"""Run many experiments. One experiment is many sets of P-Value simulations."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved."
__author__ = "DV Klopfenstein"

import sys
import numpy as np
from pkgsim.pval_sims import PvalSimMany


class Experiments(object):
    """Run many experiments. One experiment is many sets of P-Value simulations, each w/FDR correction."""

    def __init__(self, num_sims, num_pvals, perc_sig, multi_params, fnc_maxsig):
        """Simulate MANY multiple-test correction of P-values."""
        pvalsimobjs = []
        for _ in range(num_sims):
            obj1sim = PvalSimMany(self.num_pvals, self.num_sig, self.multi_params, self.max_sigval)
            pvalsimobjs.append(obj1sim)
        return pvalsimobjs

# Copyright (C) 2016-2017, DV Klopfenstein. All rights reserved.
