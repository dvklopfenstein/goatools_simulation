"""Plotting code for filling one tile of a tiled plot."""

__copyright__ = "Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved."
__author__ = "DV Klopfenstein"

import collections as cx
import seaborn as sns
import numpy as np

class PlotInfo(object):
    """Plot information for tiled plots in general and for one of various stats attributes."""

    attr2grp = {
        'fdr_actual':'FDR',
        'sensitivity':'Sensitivity',
        'specificity':'Specificity',
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
            'yticklabels':["0.000", "0.025", "0.050", "0.075"],
            'ylim':[-0.005, 0.09],
            'alphaline':True},
        'fdr_actual':{
            'plottype':'boxplot',
            'yticks':[0.00, 0.025, 0.05, 0.075],
            'yticklabels':["0.000", "0.025", "0.050", "0.075"],
            'ylim':[-0.005, 0.09],
            'alphaline':True},
        'sensitivity':{
            'plottype':'barplot',
            'yticks':[0.0, 0.25, 0.5, 0.75, 1.00],
            'yticklabels':["0.00", "0.25", "0.50", "0.75", "1.00"],
            'ylim':[-0.05, 1.05],
            'alphaline':False},
        'specificity':{
            'plottype':'barplot',
            'yticks':[0.0, 0.25, 0.5, 0.75, 1.00],
            'yticklabels':["0.00", "0.25", "0.50", "0.75", "1.00"],
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

    def get_str_mean(self, exps, desc=None):
        """Get value with x and y location to be printing inside plot."""
        valstrs = []
        if self.kws['plottype'] == 'barplot':
            ntobj = cx.namedtuple("NtValstr", "valstr x y ha va")
            left_num = exps[0].params['num_items']
            for xval, exp in enumerate(exps): # ManyHypothesesSims or ManyGoeaSims
                yval = np.mean(exp.get_means(self.attrname, desc))
                # Plot text that can comfortably fit in plot.
                if yval > 0.0001 and yval <= 0.50:
                    valstr = "{VAL:2.0f}%".format(VAL=yval*100)
                    ntplt = ntobj(valstr=valstr, x=xval, y=yval+0.05, ha='center', va='bottom')
                    valstrs.append(ntplt)
                elif yval > 0.50 and yval <= 0.99:
                    if exp.params['num_items'] != left_num or yval <= 0.75:
                        valstr = "{VAL:2.0f}%".format(VAL=yval*100)
                        ntplt = ntobj(valstr=valstr, x=xval, y=yval-0.30, ha='center', va='bottom')
                        valstrs.append(ntplt)
        return valstrs

    def _init_axes_params(self, usr_pltattr2pltnm2val):
        """Return plotting parameters that differ for various plotting values; dostsize, ylim."""
        kws = {}
        plt_attr2vals = self.dflt_attr2vals.get(self.attrname, None)
        # pltattr: dotsize plottype yticks yticklabels ylim alphaline
        for pltattr, val_dflt in self.dflt_attr2vals['dflt'].items():
            curval = None
            val_plt = plt_attr2vals.get(pltattr, None)
            # Ex: {'fdr_actual':2.00, 'sensitivity':1.00}
            usr_pltnm2val = usr_pltattr2pltnm2val.get(pltattr, None)
            if usr_pltnm2val is not None:
                curval = usr_pltnm2val.get(self.attrname, None)
            if curval is None:
                curval = val_plt if val_plt is not None else val_dflt
            kws[pltattr] = curval
        for key, val in kws.items():
            self.kws[key] = val

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
        #xpos = 0.96*axes.get_xlim()[1]
        #ypos = 0.85*kws['ylim'][1]
        #axes.text(xpos, ypos, kws['letter'], ha='right', va='center')
        xpos = axes.get_xlim()[0] + 0.05
        ypos = 0.85*kws['ylim'][1]
        axes.text(xpos, ypos, kws['letter'], ha='left', va='center')
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

def get_num_rows_cols(key2exps):
    """Return the number of rows and columns for a matrix of tiled boxplots."""
    perc_nulls, max_sigpval = zip(*key2exps.keys())
    return len(set(perc_nulls)), len(set(max_sigpval))

def get_dftbl_boxplot(experimentsets, attr='fdr_actual', grp='FDR', desc='genes'):
    """Get plotting data suitable for a single plot of boxplots."""
    tbl = []
    for exps in experimentsets: # Each expset has the same (X)max_sigpval and (Y)perc_null
        tot_h = exps.params['num_items'] # Number of hypotheses
        # Make one dictionary line for each value of fdr_actual
        dcts = [{'xval':tot_h, 'yval':y, 'group':grp} for y in exps.get_means(attr, desc)]
        tbl.extend(dcts)
    return tbl

# Copyright (C) 2016-2017, DV Klopfenstein, Haibao Tang. All rights reserved.
