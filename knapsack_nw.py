# -*- coding: utf-8 -*-
"""
Integer 01 knapsack solver using dynamic programming.
Runs in O(nW) time.

@author: Jay
"""
import pandas as pd
import numpy as np


# 0-1 Knapsack algorithm
def knapsack_nw(inv, B):
    N = len(inv)
    # initiate the memo
    memo = pd.DataFrame(np.zeros((N+1, B+1)))
    for n in range(1, N+1):
        # for each item
        inv_item = inv.iloc[n-1]
        wi = inv_item['weight']
        vi = inv_item['value']
        for w in range(0, B+1):
            # set up a no-fit
            skip = memo.iloc[n-1][w]
            mx = skip
            # if it fits
            if wi <= w:
                # consider the item
                take = vi + memo.iloc[n-1][w - wi]
                mx = max(take, skip)
            # update memo
            memo.set_value(n, w, mx)
    # return bottom right cell
    return memo.iloc[N][B]
