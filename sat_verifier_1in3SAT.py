"""
1-in-3SAT Truth Assignment Verifier. This method takes a dictionary of truth
assignment and a set of clauses as input, and checks whether the clauses
are satisified in 1-in-3SAT terms.

Parameters:
    literals: A dictionary of literal : boolean pairs. 
    clauses: A list of lists. Each sublist must contain 3 literals
                where the absolute value of each has an entry in literals
Returns:
    sat_bool: A boolean indicating whether the clauses are satisfied by the truth assignments.

@author: Jay
"""

    
# 1-in-3SAT Satisfaction tester
def verifier_1in3SAT(literals, clauses):
    # boolean list to keep track of satisfaction
    sat_list = []
    # empty set is satisfied?
    sat_bool = True
    for i in range(0, len(clauses)):
        trues = 0
        for j in range(0, len(clauses[i])):
            lit = clauses[i][j]
            # map literal to truth assignment (negative -> negated)
            if lit < 0:
                lit = abs(lit)
                if literals[lit] == False:
                    trues = trues + 1
            else:
                if literals[lit] == True:
                    trues = trues + 1
        # if exactly one true in the clause
        if trues == 1:
            sat_list.append(True)
        else:
            sat_list.append(False)
            sat_bool = False
    return sat_bool