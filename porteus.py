from __future__ import division
import random
import numpy as np

# See Porteus, Evan L. "Computing the discounted return in Markov and semi‐Markov chains." Naval Research Logistics Quarterly 28.4 (1981): 567-577.

def generateP(NR, NNZ, MAXP):
    # Generate transition matrix
    # NR = number of rows (i.e. states)
    # NNZ = maximum number of non-zero elements per row
    # MAXP = maximum probability in any row
