# SAT and Knapsack Problem Experiments

This repository contains the final project for Skidmore's Computability and Complexity class (with permission from the professor). These scripts make broad use of the Pandas library to format 2D arrays and result tables. Pandas is probably not a very efficient way to implement knapsack algorithms.

The scripts focus on two decision problems: Knapsack and 3SAT.

### Knapsack Algorithms (Solvers/Approximators)

* O(n*w) traditional knapsack dynamic programming
* O(max(V) * n^2) dynamic programming (based on min-cost)
* Fully Polynomial Time Approximation Scheme using the O(max(V) * n^2) algo and scaled values
* Greedy two-approximation based on fractional knapsack

### SAT Algorithms (Reductions)

* 3SAT -> 1-in-3SAT Reduction
* 1-in-3SAT -> Subset Sum Reduction
* Subset Sum -> Knapsack reduction

### Additional scripts 
* Instance generators for Knapsack and 3SAT
* SAT verifiers for 1-in-3SAT and 3SAT
* Experimentation main scripts to run and compare the various algorithms
