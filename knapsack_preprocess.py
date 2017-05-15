# -*- coding: utf-8 -*-
"""
Preprocessing steps for a knapsack inventory.
Steps:
    Standardize column names to weight and value
    Remove items with cost greater than the budget
    Reset the indices of the data frame

@author: Jay
"""

def knapsack_preprocess(inv, B):
    inv.columns = ['weight', 'value']
    inv = inv[inv['weight'] <= B]
    inv = inv.reset_index(drop=True)
    return inv, B
