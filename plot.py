from __future__ import division

from collections import Counter

import holoviews as hv
import numpy as np
import pandas as pd


def combined_plot(a, d, t):
    pmf = plot_PMF(t['a'], t['d'])
    cmf = plot_CMF(a, d)
    exp = plot_exp_val(a, d)
    return hv.Layout([pmf, cmf, exp])


# PMF functions and variables
pmf_opts = dict(Bars=dict(plot=dict(xrotation=45, legend_position='left',
                                    width=750, tools=['hover']),
                          style=dict(cmap='Set1')))


def PMF(total):
    return {x: y / len(total) for x, y in Counter(total).iteritems()}


def plot_PMF(total_a, total_d):
    ca, cd = PMF(total_a), PMF(total_d)
    # Create DataFrame for plot
    df = pd.DataFrame()
    df['t'] = pd.concat([pd.Series(ca), pd.Series(cd)])
    df['l'] = ['Attacker' for _ in ca] + ['Defender' for _ in cd]
    # Reset index and relabel columns
    df = df.reset_index()
    df.columns = ['Damage', 'Totals', 'Label']
    return hv.Bars(df, kdims=['Damage', 'Label'],
                   vdims='Totals', label='Probability of Damage').opts(pmf_opts)


# CMF functions and variables
def cum_sums(vals):
    cum_sums = np.cumsum(PMF(vals).values()[::-1])[::-1]
    return {x: y for x, y in zip(vals.keys(), cum_sums)}


def CMF(d):
    return melt_cmf(pd.DataFrame({x: cum_sums(d[x]) for x in d}))


def melt_cmf(df):
    df = df.reset_index()
    df = df.melt('index')
    df.columns = ['Roll', 'Type', 'Value']
    return df


cmf_opts = dict(Bars=dict(plot=dict(xrotation=80, width=750,
                                    tools=['hover'], legend_position='left')))


def plot_CMF(a, d):
    a_cmf, d_cmf = CMF(a), CMF(d)
    a_cmf['Label'] = ['Attacker' for _ in a_cmf.index]
    d_cmf['Label'] = ['Defender' for _ in d_cmf.index]
    a_bar = hv.Bars(a_cmf, kdims=['Roll', 'Type'], vdims=['Value'], label='Attacker').opts(cmf_opts)
    d_bar = hv.Bars(d_cmf, kdims=['Roll', 'Type'], vdims=['Value'], label='Defender').opts(cmf_opts)
    return hv.Layout([a_bar, d_bar])


# Expected value functions
def exp_val(x):
    df = pd.DataFrame(x.sum().divide(len(x))).reset_index()
    df.columns = ['Type', 'Value']
    return df


def plot_exp_val(a, d):
    a_bar = hv.Bars(exp_val(a), label='A-Exp-Val')
    d_bar = hv.Bars(exp_val(d), label='D-Exp-Val')
    opts = dict(Bars=dict(plot=dict(xrotation=45, legend_position='left',
                                    width=750, tools=['hover']),
                          style=dict(cmap='Set1')))
    return hv.Layout([a_bar, d_bar]).opts(opts)
