# -*- coding: utf-8 -*-
"""
Subset Sum < Knapsack Reducer. This simple reduction just
returns a set of weights (copy of values) and a budget (copy of target)

@author: Jay
"""

import pandas as pd


def reducer_ss_knapsack(items, target):
    B = target
    cols = ['weight', 'value']
    inv = pd.DataFrame(columns=cols)
    inv['weight'] = items
    inv['value'] = items
    return inv, B
