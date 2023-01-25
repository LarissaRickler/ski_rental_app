"""
Defines online algorithms used in ski_rental_app.
"""

import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt
import math



def alg_naive(b, x, y):  
    results = []
    
    for i in range(x.shape[0]):
        if y[i] >= b:
            results.append(b)
        else:
            results.append(x[i])
    return np.array(results)
    
    
def alg_det(b, x, y, tradeoff_lambda):   
    results = []
    
    for i in range(x.shape[0]):
        if y[i] >= b:
            threshold = math.ceil(tradeoff_lambda * b)
            if x[i] < threshold:
                results.append(x[i])
            else:
                results.append(threshold - 1 + b)
        else: 
            threshold = math.ceil(b / tradeoff_lambda)
            if x[i] < threshold:
                results.append(x[i])
            else:
                results.append(threshold - 1 + b)
    return np.array(results)
    
    
def prob(b, k):
    sum_q = 0
    prob_ret = rand.uniform(0, 1)
    for j in range(1, k + 1):
        q = ((b - 1) / b)**(k - j) * (1 / (b * (1 - (1 - 1 / b)**k))) 
        sum_q += q
        if prob_ret < sum_q:
            return j
    return k


def alg_rand(b, x, y, tradeoff_lambda):   
    results = []
    
    for i in range(x.shape[0]):
        if y[i] >= b:
            k = math.floor(tradeoff_lambda * b)
            threshold = prob(b, k)
            if x[i] < threshold:
                results.append(x[i])
            else:
                results.append(threshold - 1 + b)
        else: 
            l = math.ceil(b / tradeoff_lambda)
            threshold = prob(b, l)
            if x[i] < threshold:
                results.append(x[i])
            else:
                results.append(threshold - 1 + b)
    return np.array(results)


def alg_det_online(b, x):   
    return alg_det(b, x, x, 1)


def alg_rand_online(b, x):
    return alg_rand(b, x, x, 1)


def opt(b, x):
    result = np.empty(x.shape[0], dtype=np.int64)
    result.fill(b)
    result[x < b] = x[x < b]
    return result


def comp_ratio(ALG, OPT):
        return ALG / OPT