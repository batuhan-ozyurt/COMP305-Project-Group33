## Meeting 2 Minutes (1st of June, 2021)

* We went over the code of our baseline model. This is a brute-force algorithm that calculates the response times for all possible paths and chooses the best one. This algorithm is O(n!) because at first, we choose 1 database from n databases, and in the next step, we choose 1 from (n-1) databases and so on. To be precise, there are n! / 2 unique cases to be considered because a path that goes x1, x2,..., xn gives the same result as a path that goes xn,..., x2, x1.
* We figured out a way to represent our GIGGLE problem as an undirected graph. In this graph, each vertex represents a database and stores the database id, and all of the vertices are connected, hence our graph forms a clique. The weights of the edges are the absolute values of the differences between the two vertex keys, i.e. the response time of moving from one database to the other. We are asked to find a Hamiltonian cycle in this graph, and the sum of the weights should be as large as possible but smaller than the threshold.
* We also realised that if the database id's are sorted, it takes O(1) time to find the cycle with the minimum weight. It is equal to 2 times the difference of the largest number and the smallest number (0 included). So, checking if a solution exists or not is O(1).
* We detected an analogy between our GIGGLE problem and the traveling salesman problem: In both problems we are trying to find a cycle that visits all vertices. However, TSP problem is NP-complete, but finding the minimum weight cycle is O(1) in our problem.

### TODO for the next meeting

* Try to improve the baseline model that we have.
* Research on cliques and Hamiltonian cycles to come up with a more efficient algorithm.
* Think about the analogy between our problem and the TSP. Try to reduce one to another.
