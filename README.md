# T2MIR
## Indexing algorithms performance comparison

The goal here was to analise the relationship between efficiency and effectiveness between different indexes when resolving searches for the nearest neighbours.
For the following indexes a **Similarity Join of the approximate nearest neighbour** is resolved, using the implementations of the indexes found in the [FLANN library](https://github.com/mariusmuja/flann):
 
 - **Randomized KD-Tree** for different number of *trees*.
 - **K-Means Tree** for different levels of *branching*
 - **Linear Scan** or brute force algorithm. This will be our base line for comparison.
 
The following are the measurements used for comparison:

 - **Effectiveness** : Fraction of the query's made to the index which nearest neighbour is the same as the one found by the **Linear Scan**.
 - **Efficiency** : Fraction of time used for resolving all the query's in comparinson to **Linear Scan**.
 
To view the results please see the pdf file in this repository.