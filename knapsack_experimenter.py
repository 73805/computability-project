# -*- coding: utf-8 -*-
"""
Main Knapsack method. This file imports the relevant functions
and runs them while measuring some metrics

@author: Jay
"""

from knapsack_nw import knapsack_nw
from knapsack_n2v import knapsack_n2v
from knapsack_greedy2approx import knapsack_greedy2approx
from knapsack_fptas import knapsack_fptas

import pandas as pd
import pickle
import time

# Load the 100 instances
f = open('knapsack_instances.pkl', 'r')
instance_list = pickle.load(f)
f.close()



cols = ['n','budget','vsum','ratio','nw_soln','nw_time','n2v_soln','n2v_time','g2a_soln','g2a_time', 'fptas_soln','fptas_time']
results = pd.DataFrame(columns=cols)
for i in range(0, len(instance_list)):
    # unpack the instance
    instance = instance_list[i]
    inv = instance['inventory']
    B = instance['budget']
    r = instance['ratio']
    # additional meta info
    n = len(inv)
    vsum = int(sum(inv.value))

    new_row = [n, B, vsum, r]

    # Begin calling algorithms

    # nw - traditional DP
    t0 = time.clock()
    nw_soln = knapsack_nw(inv, B)
    t1 = time.clock()
    nw_time = t1 - t0
    new_row.append(nw_soln)
    new_row.append(nw_time)

    # n2v - DP based on min cost
    t0 = time.clock()
    n2v_soln = knapsack_n2v(inv, B)
    t1 = time.clock()
    n2v_time = t1 - t0
    new_row.append(n2v_soln)
    new_row.append(n2v_time)

    # Greedy 2-approximation
    t0 = time.clock()
    g2a_soln = knapsack_greedy2approx(inv, B)
    t1 = time.clock()
    g2a_time = t1 - t0
    new_row.append(g2a_soln)
    new_row.append(g2a_time)

    # FPTAS Algorithm with approx ratio r
    t0 = time.clock()
    fptas_soln = knapsack_fptas(inv, B, r)
    t1 = time.clock()
    fptas_time = t1 - t0
    new_row.append(fptas_soln)
    new_row.append(fptas_time)

    print "Writing to results: " + str(i)
    results.loc[-1] = new_row
    results.index = results.index + 1

results = results.reset_index(drop=True)
results['fptas_soln_quality'] =results['fptas_soln'] / results['nw_soln']
results['g2a_soln_quality'] = results['g2a_soln'] / results['nw_soln']

results.to_pickle('knapsack_results.pkl')