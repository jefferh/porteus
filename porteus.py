import time
import random
import numpy as np

# See the appendix in Porteus, Evan L. "Computing the discounted return in Markov and semi-Markov chains." Naval Research Logistics Quarterly 28.4 (1981): 567-577.

def generateP(NR, NNZ, MINP, MAXP):
    # Generate transition matrix
    # NR = number of rows (i.e. states)
    # NNZ = maximum number of non-zero elements per row
    # MINP = minimum probability in any row
    # MAXP = maximum probability in any row

    start_time = time.time()
    
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
    print("Time to generate transition probabilities: %s seconds" % (time.time()-start_time))
    return P

def generateR(NR):
    # Generate one-step rewards
    # NR = number of rows (i.e. states)

    R = np.zeros(shape=(NR,1))
    for i in range(10):
        R[i] = 10*(i+1)
    if NR > 10:
        for i in range(10,NR):
            R[i] = np.random.uniform()
        R[NR-1] = 0
    return R
