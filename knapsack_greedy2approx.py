# -*- coding: utf-8 -*-
"""
Integer 01 Knapsack greedy 2 approximator

@author: Jay
"""
import pandas as pd


def knapsack_greedy2approx(inv, B):
    # add the ratio column, and sort by it
    inv['ratio'] = inv['value'] / inv['weight']
    inv.sort_values(by='ratio', ascending=False, inplace=True)
    inv = inv.reset_index(drop=True)

    # prepare the knapsack
    N = len(inv)
    i = 0
    knap = pd.DataFrame(columns=['weight', 'value', 'ratio'])
    # fill knapsack while budget and inventory are not empty
    while B != 0 and i < N:
        inv_item = inv.iloc[i]
        wi = inv_item['weight']
        if wi <= B:
            B = B - wi
            knap.loc[-1] = inv_item
            knap.index = knap.index + 1

        i = i + 1

    knap = knap.reset_index(drop=True)
    # compare largest item to knap
    mx = max(max(inv['value']), sum(knap['value']))
    return mx
