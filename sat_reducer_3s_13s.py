"""
3SAT < 1-in-3SAT Reduction Function. This function takes a 3SAT 
instance as input and returns an instance mapping reduction in 1-in-3SAT form. 
A new set of clauses are built, and the new literals are added to dictionary
from the position of the max value literal in the original instance.

Parameters:
    literals: A dictionary of literal : boolean pairs. 
    clauses: A list of lists. Each sublist must contain 3 literals
                where the absolute value of each has an entry in literals
Returns:
    literals: The dictionary of clause literal : Boolean pairs
    clauses: A list of numClause clauses. Each sublist contains 3 literals.
    
@author: Jay
"""

# 3SAT to 1-in-3SAT reducer
def reducer_3s_13s(literals, clauses):
    new_clauses = []
    new_literals = literals.copy()
    created_literals = {}
    lit_pointer = max(new_literals.keys()) + 1
    for i in range(0, len(clauses)):
        clause = clauses[i]
        x1, x2, x3 = clause
        # add extra literals to end of extras
        a, b, c, d = range(lit_pointer, lit_pointer+4)
        lit_pointer = lit_pointer + 4
        c1 = [-x1,  a,   b]
        c2 = [  b, x2,   c]
        c3 = [  c,  d, -x3]
        # append replacement clauses
        new_clauses.append(c1)
        new_clauses.append(c2)
        new_clauses.append(c3)
        created_literals[a] = False
        created_literals[b] = False
        created_literals[c] = False
        created_literals[d] = False

    # merge original literal dictionary with the created literals
    new_literals.update(created_literals)
    return new_literals, new_clauses