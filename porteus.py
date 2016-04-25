from __future__ import division
import random
import numpy as np

# See Porteus, Evan L. "Computing the discounted return in Markov and semi-Markov chains." Naval Research Logistics Quarterly 28.4 (1981): 567-577.

def generateP(NR, NNZ, MINP, MAXP):
    # Generate transition matrix
    # NR = number of rows (i.e. states)
    # NNZ = maximum number of non-zero elements per row
    # MINP = minimum probability in any row
    # MAXP = maximum probability in any row
    
    P = np.zeros(shape=(NR,NR))
    numGenProb = 0
    rowSum = 0
    for i in range(NR): # for each row in the transition matrix
        while numGenProb < NNZ and rowSum < 1:        
            # generate another transition probability
            numGenProb += 1
            indsZero = [ind for ind,val in enumerate(P[i,:]) if val == 0] 
            loc = random.choice(indsZero) # randomly pick a destination state with zero transition probability
            REM = 1 - rowSum
            if numGenProb == NNZ:
                P[i,loc] = REM
            else:
                P[i,loc] = np.random.uniform(low=MINP, high=min(MAXP,REM))
            rowSum += P[i,loc]
        numGenProb = 0
        rowSum = 0
    return P
