# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 20:54:14 2017

@author: Jay
"""

from knapsack_n2v import knapsack_n2v
import pandas as pd
import numpy as np

def knapsack_fptas(inv, B, tol):
    N = len(inv)
    
    vmax = max(inv.value)
    fact = float(tol) * (vmax / N)
    inv.value = np.floor(inv.value / fact)
    
    appsoln = knapsack_n2v(inv, B) * fact
    return appsoln