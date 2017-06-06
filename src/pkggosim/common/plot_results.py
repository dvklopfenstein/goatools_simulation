"""Plotting code for filling one tile of a tiled plot."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import collections as cx
import seaborn as sns
import pandas as pd
import numpy as np

class PlotInfo(object):
    """Plot information for tiled plots in general and for one of various stats attributes."""

    attr2grp = {
        'fdr_actual':'FDR',
        'sensitivity':'Sensitivity',
    }

    dflts_plt = {
        'grpname':None,
        'dpi':400,
        'title':'Hypotheses Simulations',
        'xlabel':'Number of Tested Hypotheses',
        'ylabel':'Simulated {GRP} Ratios',
        'txtsz_title':20,
        'txtsz_xy'   :17,
        'txtsz_tile' :None,
        'txtsz_ticks':None,
    }

    dflt_attr2vals = {
        'dflt':{
            'dotsize':1.0,
            'plottype':'boxplot',
            'yticks':[0.00, 0.025, 0.05, 0.075],
            'yticklabels':["", "0.025", "0.050", "0.075"],
            'ylim':[0.0, 0.09],
            'alphaline':True},
        'fdr_actual':{
            'plottype':'boxplot',
            'yticks':[0.00, 0.025, 0.05, 0.075],
            'yticklabels':["", "0.025", "0.050", "0.075"],
            'ylim':[0.0, 0.09],
            'alphaline':True},
        'sensitivity':{
            'plottype':'barplot',
            'yticks':[0.0, 0.25, 0.5, 0.75, 1.00],
            'yticklabels':["", "0.25", "0.50", "0.75", "1.00"],
            'ylim':[-0.05, 1.05],
            'alphaline':False},
    }

    def __init__(self, attrname, args_kws):
        self.attrname = attrname
        self.kws = {key:args_kws.get(key, dfltval) for key, dfltval in self.dflts_plt.items()}
        _grpname = self.kws['grpname']
        self.grpname = _grpname if _grpname is not None else self.attr2grp[self.attrname]
        # Update ylabel with friendlier text
        if 'ylabel' not in args_kws:
            self.kws['ylabel'] = self.kws['ylabel'].format(GRP=self.grpname)
        self._init_axes_params(args_kws)

    def get_str_mean(self, exps):
        """Get value with x and y location to be printing inside plot."""
        valstrs = []
        if self.attrname == "sensitivity":
            ntobj = cx.namedtuple("NtValstr", "valstr x y")
            for xval, exp in enumerate(exps): # ManyHypothesesSims or ManyGoeaSims
                val = np.mean(exp.get_means(self.attrname))
                # Plot text that can comfortably fit in plot.
                if val > 0.0001 and val < 0.75:
                    valstr = "{VAL:2.0f}%".format(VAL=val*100)
                    valstrs.append(ntobj(valstr=valstr, x=xval, y=val+0.05))
        return valstrs

    def _init_axes_params(self, usr_pltattr2pltnm2val):
        """Return plotting parameters that differ for various plotting values; dostsize, ylim."""
        print "AAAAAA", usr_pltattr2pltnm2val
        kws = {}
        plt_attr2vals = self.dflt_attr2vals.get(self.attrname, None)
        # pltattr: dotsize plottype yticks yticklabels ylim alphaline
        for pltattr, val_dflt in self.dflt_attr2vals['dflt'].items():
            curval = None
            val_plt = plt_attr2vals.get(pltattr, None)
            # Ex: {'fdr_actual':2.00, 'sensitivity':1.00}
            usr_pltnm2val = usr_pltattr2pltnm2val.get(pltattr, None)
            print "PPPPPP", pltattr, val_dflt, usr_pltnm2val
            if usr_pltnm2val is not None:
                curval = usr_pltnm2val.get(self.attrname, None)
            if curval is None:
                curval = val_plt if val_plt is not None else val_dflt
            kws[pltattr] = curval
        for k, v in kws.items():
            self.kws[k] = v
            print "WWWWWW", k, v


def fill_axes(axes, dfrm, alpha, **kws):
    """Fills axes axes with one set of boxplots of simulated FDRs."""
    lwd = kws.get('linewidth', 0.7)
    dotsz = kws.get('dotsize', 5)
    plottype = kws.get('plottype', "boxplot")
    pal = 'dark' # Seaborn color palette
    plt_data = {'x':"xval", 'y':"yval", 'data':dfrm, 'ax':axes}
    sns.stripplot(jitter=True, size=dotsz, palette=pal, **plt_data)
    if plottype == 'boxplot':
        sns.boxplot(hue="group", linewidth=lwd, color='black', saturation=1, **plt_data)
        axes.legend_.remove()
    elif plottype == 'barplot':
        sns.barplot(palette=pal, alpha=.3, saturation=1, ci=None, **plt_data)
    _set_color_whiskers(axes, lwd, 'black', 'red')
    _set_color_boxes(axes, 'black')
    if alpha is not None:
        axes.plot([-1000, 1000], [alpha, alpha], 'k--', alpha=1.0,
                  linewidth=lwd, solid_capstyle="butt")
    if 'ylim' in kws:
        axes.set_ylim(kws['ylim'])
    if 'title' in kws:
        axes.set_title(kws['title'], size=25)
    axes.set_xlabel(kws.get('xlabel', ""), size=20)
    axes.set_ylabel(kws.get('ylabel', ""), size=20)
    if 'letter' in kws and 'ylim' in kws:
        xpos = 0.96*axes.get_xlim()[1]
        ypos = 0.85*kws['ylim'][1]
        axes.text(xpos, ypos, kws['letter'], ha='right', va='center')
    return axes

def _set_color_whiskers(axes, lwd, col_end, col_mid):
    """Set boxplot whisker line color and thinkness."""
    for i, line in enumerate(axes.lines):
        line.set_linewidth(lwd)
        is_median = i%6 == 4
        line.set_color(col_mid if is_median else col_end)
        if is_median:
            line.set_linestyle('--')

def _set_color_boxes(axes, color):
    """Set boxplot box line color."""
    for artist in axes.artists:
        artist.set_edgecolor(color)

# TBD move to hypothesis/plot_results
def plt_tile(idx, num_rows, num_cols, tile_items, objplt):
    """Plot one tile of a multi-tiled plot."""
    kws = objplt.kws
    (axes, ((perc_null, maxsig), exps)) = tile_items
    letter = "{C}{R}".format(R=idx/num_cols+1, C=chr(65+idx%num_cols))
    dfrm = pd.DataFrame(get_dftbl_boxplot(exps, objplt.attrname, objplt.grpname))
    alpha = exps[0].alpha if kws['alphaline'] else None
    fill_axes(axes, dfrm, alpha, dotsize=kws['dotsize'],
              plottype=kws['plottype'], letter=letter, ylim=kws['ylim'])
    axes.set_xticklabels([e.params['num_items'] for e in exps], size=kws['txtsz_ticks'])
    axes.set_yticks(kws['yticks'])
    axes.set_yticklabels(kws['yticklabels'])
    if idx >= num_cols*(num_rows-1): # bottom_row
        axes.set_xlabel("Sig.<={MAXSIG}".format(MAXSIG=maxsig), size=kws['txtsz_tile'])
    if idx%num_cols == 0:
        axes.set_ylabel("{PERCNULL}% Null".format(PERCNULL=perc_null), size=kws['txtsz_tile'])
    axes.set_ylim(kws['ylim'])
    axes.tick_params('both', length=3, width=1) # Shorten both x and y axes tick length
    # Add value text above plot bars to make plot easier to read
    for ntval in objplt.get_str_mean(exps):
        axes.text(ntval.x, ntval.y, ntval.valstr, ha='center', va='bottom')

def get_tiled_axes(fig, n_rows, n_cols):
    """Create empty axes to be filled and used in tiled boxplot image."""
    ax1 = fig.add_subplot(n_rows, n_cols, 1)
    rng = range(2, n_rows*n_cols+1)
    return [ax1] + [fig.add_subplot(n_rows, n_cols, i, sharex=ax1, sharey=ax1) for i in rng]

def tiled_xyticklabels_off(axes, num_cols):
    """Turn off xticklabels and yticklabels on the inside plot edges of the tiled boxplots."""
    for xaxis in axes[:-1*num_cols]:
        for label in xaxis.get_xticklabels():
            label.set_visible(False)
    for idx, yaxis in enumerate(axes):
        if idx%num_cols != 0:
            for label in yaxis.get_yticklabels():
                label.set_visible(False)

def get_num_rows_cols(key2exps):
    """Return the number of rows and columns for a matrix of tiled boxplots."""
    perc_nulls, max_sigpval = zip(*key2exps.keys())
    return len(set(perc_nulls)), len(set(max_sigpval))

def get_dftbl_boxplot(experimentsets, attr='fdr_actual', grp='FDR'):
    """Get plotting data suitable for a single plot of boxplots."""
    tbl = []
    for exps in experimentsets: # Each expset has the same (X)max_sigpval and (Y)perc_null
        tot_h = exps.params['num_items'] # Number of hypotheses
        # Make one dictionary line for each value of fdr_actual
        dcts = [{'xval':tot_h, 'yval':y, 'group':grp} for y in exps.get_means(attr)]
        tbl.extend(dcts)
    return tbl

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
