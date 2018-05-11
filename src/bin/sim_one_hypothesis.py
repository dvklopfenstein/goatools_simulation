#!/usr/bin/env python
"""Small number of Hypothesis sims w/various P-values to explore "True null" and target."""
# https://github.com/tanghaibao/goatools/issues/99

from __future__ import print_function

__copyright__ = "Copyright (C) 2016-2018, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

from pkggosim.common.randseed import RandomSeed32
from pkggosim.hypotheses.sim import HypothesesSim


def main():
    """P-values at various levels for "True null" and target."""
    RandomSeed32(42)
    max_sigpvals = [0.0001, 0.001, 0.01]
    perc_nulls = [95]  # [100, 75, 50, 25],
    num_hypoths_list = [100]  # [4, 16, 128],

    for hypoth_qty in num_hypoths_list:  # [4, 16, 128]
        for max_sigpval in max_sigpvals:
            for perc_null in perc_nulls:
                num_null = int(round(float(perc_null)*hypoth_qty/100.0))
                print("{hypoth_qty}=hypoth_qty {num_null}=num_null {max_sigpval}=max_sigpval".format(
                    hypoth_qty=hypoth_qty, num_null=num_null, max_sigpval=max_sigpval))
                obj = HypothesesSim(
                    hypoth_qty,
                    num_null,
                    multi_params={'alpha' : 0.05, 'method' : 'fdr_bh'},
                    max_sigval=max_sigpval,
                    pval_surge=None)
                print(obj.nt_tfpn)
                for idx, ntg in enumerate(sorted(obj.nts_pvalnt, key=lambda nt: nt.pval)):
                    diff = ntg.pval_corr - ntg.pval
                    print("{:8.6f}".format(diff), ntg)
                    if idx == 10:
                        print("...")
                        break
                print("")


if __name__ == '__main__':
    main()

# Copyright (C) 2016-2018, DV Klopfenstein, Haibao Tang. All rights reserved.
