import sys
import numpy as np
import random
import math

def Multivariate_Normal(size, cov):
    # step 1 - get normally distributed data
    X1 = np.array([box_muller()[0] for x in range(size)])
    X2 = np.array([box_muller()[0] for x in range(size)])

    # step 2 - reshape
    X = np.vstack([X1, X2]).T
    reshaped_data = np.dot(X, cov)
    X1_reshaped = reshaped_data[:,0]
    X2_reshaped = reshaped_data[:,1]
    return X1_reshaped, X2_reshaped
    
def box_muller():
    epsilon = sys.float_info.epsilon

    u1, u2 = 0.0, 0.0
    while u1 < epsilon or u2 < epsilon:  # Avoid getting u == 0.0
        u1 = random.random()
        u2 = random.random()

    n1 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
    n2 = math.sqrt(-2 * math.log(u1)) * math.sin(2 * math.pi * u2)
    return n1, n2