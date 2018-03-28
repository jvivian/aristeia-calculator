from die import die
from collections import defaultdict
import pandas as pd
import numpy as np

def simulate_dists(die, n_rolls=10000):
    """Return percentages for each possible die value"""
    # Define dictionary for counting values
    dists = defaultdict(list)
    for _ in xrange(n_rolls):
        # Add value if present
        for glyph, value in die.iloc[np.random.randint(0, 6)].iteritems():
            dists[glyph].append(value)
    return dists

def counts_to_probabilities(counts):
    n = len(counts.values()[0]) # Grab length from random count value
    # Convert v in each k, v pair to a Counter object 
    counts = {k: dict(Counter(v)) for k, v in counts.iteritems()}
    # Normalize each count by number of counts    
    counts = {k: {x: float(y) / n for x, y in v.iteritems()} for k, v in counts.iteritems()}
    return pd.DataFrame(counts).replace(np.nan, 0)

def hash_die_probabilties(die, n_rolls=100000, hdf_path='./die-probs.hdf'):
    """Store simulated die probabilities in HDF file"""
    for d, df in die.iteritems():
        dists = simulate_dists(die[d], n_rolls=n_rolls)
        probs = counts_to_probabilities(dists)
        probs.to_hdf(hdf_path, key=d)
