# -*- coding: utf-8 -*-
"""
3SAT Instance generator. The following method produces 3SAT instances.
Each clause is represented as a list of integers or negative integers
where 1 corresponds to x1 and -5 corresponds to negated(x5).
A dictionary of literals and truth assignments is also generated
with False as the default value for each literal.
The literals are generated randomly but will be populated incrementally
so the first clause always consists of some combination of x1, x2, x3.

Parameters:
    count: The number of instances to generate.
    maxLiteralsRange: The range of values for each instance to draw its 
                maxLiteral count from.
    numClausesRange: The range of values for each instance to draw its
                clause count from.
Returns:
    instance_list: A list of dictionaries. Each dictionary contains a
            'literals' and 'clauses' key corresponding to a single instance's
            data.
    
Notes: 
    Mapping -1 to the inverse of literals[1] must be handled by verifiers.
    Duplicate clauses may be created, especially with imbalanced parameters.

@author: Jay
"""
import random
import pickle


# Instance Generator to create 3SAT instances
# No guarentees about the number of times each literal occurs.
# May create duplicate clauses.
def satInstanceGen(count, maxLiteralsRange, numClausesRange):
    instance_list = []
    for i in range(0, count):
        maxLiterals = random.randint(maxLiteralsRange[0], maxLiteralsRange[1])
        numClauses = random.randint(numClausesRange[0], numClausesRange[1])
        literalDict = {}
        clauses = []
        inc = 1
        seenMap = {}
        # each clause is a list of 3 literals (labelled by numbers)
        for j in range(0, numClauses):
            # put three different literaks from the literalsRange in a clause together
            literalOpts = range(1, maxLiterals + 1)
            l1 = random.choice(literalOpts)
            literalOpts.remove(l1)
            l2 = random.choice(literalOpts)
            literalOpts.remove(l2)
            l3 = random.choice(literalOpts)
            lits = [l1, l2, l3]
            for k in range(0, len(lits)):
                # map random values to 1,2,3... based on the order they are seen
                lit = lits[k]
                if lit not in seenMap.keys():
                    seenMap[lit] = inc
                    inc = inc + 1
                # map to ordered values
                lit = seenMap[lit]
                # add to the truth setting dictionary
                literalDict[lit] = False
                lits[k] = lit
            lits.sort()
            for k in range(0, len(lits)):
                # maybe 'negate' the literal by inverting
                lits[k] = lits[k] * random.choice([-1, 1])
            # add to clause set
            clauses.append(lits)
        instance = {'clauseList': clauses, 'literalDict': literalDict}
        instance_list.append(instance)
    # pickle the instances ~600kb. Not very big!
    f = open('3sat_instances_small.pkl', 'w')
    pickle.dump(instance_list, f)
    f.close()

satInstanceGen(100, [4, 6], [2, 3])