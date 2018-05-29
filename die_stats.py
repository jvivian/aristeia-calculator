import sys
from collections import defaultdict

import numpy as np
import pandas as pd


def roll_die_pool(die, counts):
    dists = defaultdict(list)
    for choice, num_die in counts.iteritems():
        for _ in xrange(num_die):
            for glyph, value in die[choice].iloc[np.random.randint(0, 6)].iteritems():
                dists[glyph].append(value)
    return pd.DataFrame(dists)


def roll(die, attacker, defender, n_rolls=1000):
    # TODO: Add dynamic roll storage. Precheck for hash here, otherwise run algorithm

    # Objects to hold counts
    a_rolls, d_rolls = [], []
    t_total = defaultdict(list)

    # Convert attacker / defender widgets to die counts
    a_counts = {x: y.value for x, y in attacker.iteritems()}
    d_counts = {x: y.value for x, y in defender.iteritems()}

    # Simulate n_rolls
    for _ in xrange(n_rolls):

        # Roll attacker pool
        a_pool = roll_die_pool(die, a_counts)
        a_raw_pool = a_pool.copy()  # We want to record an unadulterated set for attacker distributions

        # Roll defender pool
        d_pool = roll_die_pool(die, d_counts)

        # Calculate total diffs
        a = pd.Series({x: sum(y) for x, y in a_pool.iteritems()})
        d = pd.Series({x: sum(y) for x, y in d_pool.iteritems()})

        # Check die aren't empty
        if 'crit' not in a.index or 'crit' not in d.index:
            print 'Dice not selected for both attacker and defender! ' \
                  '\nSelect dice for both and re-run cell again.'
            sys.exit(1)

        # If crit-defense die, drop roll with highest number of hits
        # TODO: Improve logic for removing most glyphs if tie
        # Doesn't handle crit attack die
        if d.crit_defense:
            a_pool = a_pool.drop(a_pool.hit.idxmax())
            a = pd.Series({x: sum(y) for x, y in a_pool.iteritems()})

        a_diff = a.hit - d.defense if (a.hit - d.defense) > 0 else 0
        d_diff = d.hit - a.defense if (d.hit - a.defense) > 0 else 0

        # Add crits, which are unaffected by defense
        a_diff += a.crit

        # Update totals
        a_rolls.append(a_raw_pool.sum())
        d_rolls.append(d_pool.sum())
        t_total['a'].append(a_diff)
        t_total['d'].append(d_diff)

    return pd.concat(a_rolls, axis=1).T, pd.concat(d_rolls, axis=1).T, t_total
