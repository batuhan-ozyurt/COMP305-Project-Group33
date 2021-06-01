# COMP305-Project

**Group Number: 33**

**Members:**

- Batuhan Özyurt

- Nehir Arya Taş

- Mohammad Kefah Issa

- Aydın Özcan

**To-Do List**

- Create a Baseline Model



## Meeting 1 Minutes (10th of May, 2021)

We discussed the problem and discussed multiple possible
solutions, finding counter examples for some of those
solutions and agreeing continue investigating the other
solutions.

### First Idea (zig zag)

1. Sort the database array
2. from 0 jump to the highest absolute value database
3. jump to lowest unvisited database
4. jump to highest unvisited database
5. if not at 0, go to step 3.
6. return the sum of all jumps.

Did not work, failed with the following counter case:

```
1
5
-15 0 1 5 10
60
```

### Second Idea (zig zag from all)

1. Pick a database (other than zero) that was not started from previously.
2. from 0 jump to that database.
3. jump to lowest unvisited database.
4. jump to highest unvisited database.
5. if not at 0, go to step 3.
6. store the sum of all jumps.
7. go to step 1.
8. return the heights sum recorded.

### Third Idea (Scheduling meetings?)

1. Convert jumps into weighted "meetings"
2. schedule them avoiding conflicts somehow?

```
-15 10: (25)
-15 05: (20)
-15 01: (16)
-15 00: (15)
 00 10: (10)
 01 10: (09)
 00 05: (05)
 05 10: (05)
 01 05: (04)
 00 01: (01)
```

### Fourth Idea (all possible paths)

1. from zero recurse by jumping to all other databases. 
2. recurse by jumping to all other unvisited databases. (maybe use dynamic programming to reduce complexity)
3. from all of the possible paths, return the one with highest value.


### Extra notes

We might have ignored the fact that we need to
find the longest response time **within a
threshold**, meaning that for the same database
array (input), changing the threshold can change the
correct answer (output).

## Meeting 2 Minutes (1st of June, 2021)

* We went over the code of our baseline model. This is a brute-force algorithm that calculates the response times for all possible paths and chooses the best one. This algorithm is O(n!) because at first, we choose 1 database from n databases, and in the next step, we choose 1 from (n-1) databases and so on. To be precise, there are n! / 2 unique cases to be considered because a path that goes x1, x2,..., xn gives the same result as a path that goes xn,..., x2, x1.
* We figured out a way to represent our GIGGLE problem as an undirected graph. In this graph, each vertex represents a database and stores the database id, and all of the vertices are connected, hence our graph forms a clique. The weights of the edges are the absolute values of the differences between the two vertex keys, i.e. the response time of moving from one database to the other. We are asked to find a Hamiltonian cycle in this graph, and the sum of the weights should be as large as possible but smaller than the threshold.
* We also realised that if the database id's are sorted, it takes O(1) time to find the cycle with the minimum weight. It is equal to 2 times the difference of the largest number and the smallest number (0 included). So, checking if a solution exists or not is O(1).
* We detected an analogy between our GIGGLE problem and the traveling salesman problem: In both problems we are trying to find a cycle that visits all vertices. However, TSP problem is NP-complete, but finding the minimum weight cycle is O(1) in our problem.

### TODO for the next meeting

* Try to improve the baseline model that we have.
* Research on cliques and Hamiltonian cycles to come up with a more efficient algorithm.
* Think about the analogy between our problem and the TSP. Try to reduce one to another.
 
