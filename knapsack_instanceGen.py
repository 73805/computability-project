# -*- coding: utf-8 -*-
"""
Knapsack instance generator. Each instance is a dataframe with columns
for weight and value. There are 100 items each with a weight and value
between 1 and 50. The budget is a random value between 100 and 200.
The ratio is set to 3 for the sake of future interpretation. The completed
instance is saved to a pickle file for future access.

@author: Jay
"""
from knapsack_preprocess import knapsack_preprocess

import pandas as pd
from random import randint
import pickle


def knapInstanceGen(count, n, w_range, v_range, b_range, r):
    instance_list = []
    cols = ['weight', 'value']
    for i in range(0, count):
        # generate an instance
        inv = pd.DataFrame(columns=cols)
        for j in range(0, n):
            w = randint(w_range[0], w_range[1])
            v = randint(v_range[0], v_range[1])
            inv.loc[-1] = [w, v]
            inv.index = inv.index + 1

        B = randint(b_range[0], b_range[1])
        # preprocessor removes items with weights higher than B
        inv, B = knapsack_preprocess(inv, B)

        instance = {"inventory": inv, "budget": B, "ratio": r}
        instance_list.append(instance)

    # pickle the instances ~600kb. Not very big!
    f = open('knapsack_instances.pkl', 'w')
    pickle.dump(instance_list, f)
    f.close()


knapInstanceGen(100, 100, [1, 50], [1, 50], [100, 200], 4)
