"""
1-in-3SAT < Subset Sum Reduction Function. This function takes a
1-in-3SAT instance and returns an instance mapping reduction in
SubsetSum form. The return is in the form of a dataframe where
the first n columns correspond to literals in the original instance and
the following n to n+m columns correspond to clauses in the original instance.
The rows correspond to the positive and negative versions of each literal.

Parameters:
    literals: A dictionary of literal : boolean pairs. 
    clauses: A list of lists. Each sublist must contain 3 literals
                where the absolute value of each has an entry in literals
Returns:
    items: A list of n+m item value converted from the rows of a dataframe
    target: The target value for the subset sum instance.
            Equivalent to an array of 1's with n+m entries.

@author: Jay
"""

import pandas as pd
import numpy as np


# 1-in-3SAT to Subset Sum reduce
def reducer_13s_ss(literals, clauses):
    n = len(literals)
    m = len(clauses)
    # initiate truth-setting columns of table
    df = pd.DataFrame(np.zeros((n*2, n)))
    # each literal takes two rows (normal, and negated)
    # fill in truth-setting columns (0:n)
    for i in range(0, n*2):
        df.set_value(i, i/2, 1)

    # fill in clause columns (n:n+m)
    for i, clause in enumerate(clauses):
        # clause column names c1, c2, c3...
        name = "c" + str(i)
        # initiate new column
        col = [0.0] * (n*2)
        # put 1s in corresponding rows
        for lit in clause:
            if lit > 0:
                idx = (lit - 1) * 2
            else:
                lit = abs(lit)
                idx = ((lit - 1) * 2) + 1
            col[idx] = 1
        # add the new column to the dataframe
        df[name] = col

    # convert to a list of items
    items = []
    for i in range(0, len(df)):
        row = list(df.iloc[i])
        item = list_to_int(row)
        items.append(item)
    # calcualte and convert the target
    target = [1] * (n + m)
    target = list_to_int(target)

    return items, target


# convert a list of binary values to the place value integer equivalent
def list_to_int(l):
    t = [int(i) for i in l]
    t = [str(i) for i in t]
    t = ''.join(t)
    return long(t)
