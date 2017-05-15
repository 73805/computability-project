# -*- coding: utf-8 -*-
"""
SAT Experimenter . This file imports the SAT instances
and reduction functions, and runs them while tracking
run time and result metrics.

@author: Jay
"""

# unused, but cool
from sat_instanceGen import satInstanceGen
from sat_verifier_3SAT import verifier_3SAT
from sat_verifier_1in3SAT import verifier_1in3SAT
from sat_reducer_3s_13s import reducer_3s_13s
from sat_reducer_13s_ss import reducer_13s_ss
from sat_reducer_ss_knapsack import reducer_ss_knapsack

import pandas as pd
import time
import pickle
import math

# Load the 100 instances
f = open('3sat_instances_large.pkl', 'r')
instance_list_large = pickle.load(f)
f.close()

f = open('3sat_instances_small.pkl', 'r')
instance_list_small = pickle.load(f)
f.close()

# Set up a results table for the small and large instances
cols_small = ['clauses', 'literals', '1in3_time', '1in3_clauses', '1in3_literals', 'ss_time', 'ss_log10_min_value', 'ss_log10_target', 'ss_items', 'knap_time', 'knap_n', 'knap_budget', 'knap_vsum']
cols_large = ['clauses', 'literals', '1in3_time', '1in3_clauses', '1in3_literals', 'ss_time', 'ss_log10_min_value', 'ss_log10_target', 'ss_items']
results_small = pd.DataFrame(columns=cols_small)
results_large = pd.DataFrame(columns=cols_large)

for size in ['small', 'large']:
    # Splitting for small and large
    if size == 'small':
        instance_list = instance_list_small
    if size == 'large':
        instance_list = instance_list_large

    for i in range(0, len(instance_list)):
        # unpack the instance
        clauses = instance_list[i]['clauseList']
        literals = instance_list[i]['literalDict']
        # additional meta data
        literal_count = len(literals)
        clause_count = len(clauses)

        new_row = [clause_count, literal_count]

        # Begin calling algorithms

        # 3SAT to 1-in-3SAT
        t0 = time.clock()
        literals, clauses = reducer_3s_13s(literals, clauses)
        t1 = time.clock()
        in3_time = t1 - t0
        new_row.append(in3_time)
        new_row.append(len(clauses))
        new_row.append(len(literals))

        # 1-in-3SAT to Subset Sum
        t0 = time.clock()
        items, target = reducer_13s_ss(literals, clauses)
        t1 = time.clock()
        ss_time = t1 - t0
        new_row.append(ss_time)
        new_row.append(math.log(min(items), 10))
        new_row.append(math.log(target, 10))
        new_row.append(len(items))

        # Subset Sum to Knapsack
        if size == 'small':
            t0 = time.clock()
            inv, B = reducer_ss_knapsack(items, target)
            t1 = time.clock()
            # favorite var
            knap_time = t1 - t0
            new_row.append(knap_time)
            new_row.append(len(inv))
            new_row.append(B)
            new_row.append(int(sum(inv.value)))

            # write the new row to the results table
            results_small.loc[-1] = new_row
            results_small.index = results_small.index + 1
        if size == 'large':
            # write the new row to the results table
            results_large.loc[-1] = new_row
            results_large.index = results_large.index + 1

        print "Writing to results: " + str(i)

results_small = results_small.reset_index(drop=True)
results_large = results_large.reset_index(drop=True)

results_small.to_pickle('sat_results_small.pkl')
results_large.to_pickle('sat_results_large.pkl')
