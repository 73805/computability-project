# -*- coding: utf-8 -*-
"""
Integer 01 min-cost knapsack solver using dynamic programming.
Runs in O(n^2 * Vmax) time. More precisely, the table built by this
implementation is n x Vsum. The latter term -- sum(V) is bounded by n*Vmax.

@author: Jay
"""
import pandas as pd
import numpy as np


# 0-1 Knapsack algorithm
def knapsack_n2v(inv, B):
    N = len(inv)
    # Build a min-cost memo to the max possible cost
    maxVal = int(sum(inv.value))
    memo = pd.DataFrame(np.zeros((N+1, maxVal+1)))
    # Begin building the memo
    # base line: 0, inf, inf ...
    for t in range(1, maxVal+1):
        memo.set_value(0, t, float('inf'))
    
    # fill the n x sum(values) memo
    for n in range(1, N+1):
        # for each item
        inv_item = inv.iloc[n-1]
        wi = inv_item.weight
        vi = inv_item.value
        for t in range(1, maxVal+1):
            tvi = t - vi
            if tvi < 0:
                tvi = 0
            skip = memo.iloc[n-1][t]
            take = memo.iloc[n-1][tvi] + wi
            mn = min(take, skip)
            memo.set_value(n, t, mn)
    
    # search the memo right to left, bottom to top, to find 
    # first instance of a min-cost <= budget
    opt = 0
    while t >= 0:
        n = N
        while n >= 0:
            cur = memo.iloc[n][t]
            # save a little time
            if cur == float('inf'):
                n = -10
            if cur <= B:
                opt = t
                n = -10
                t = -10
            n = n - 1
        t = t - 1

    return opt
