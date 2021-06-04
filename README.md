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
 
## Meeting 3 Minutes (2nd of June, 2021)

In this meeting we talked about the recursive solution we have now, and how
memorization is helping.

We know that the algorithms worst case complexity is O(n!), as we are
technically trying out all the possible paths, similar to the complexity of
finding all the permutations of a given string of unique characters.

However, when we started counting the number of recursive calls and tested the
algorithm with (18308) and without (149920) memoization we noticed a speed
poost attributed to the reduced ratio (12%) of recursive calls.

```
; 18308/149920
	~0.12211846318036286019
```

Not only that, but when we tested it with a lengthier input, we noticed that
the results with (1240496) and without (19663005) memoization still were
considerably better, not to mention that we were not able to wait for the one
without memoization to finish so the new ratio (6%) might be even larger than
reported. Therefore, we are confident that the increased ratio is signifying
that the improvement due to memoization is not mearly a constant, but rather a
variable dependent on n.

## Meeting 4 Minutes (4th of June, 2021)

In this meeting we will discuss the newly added "hybrid" implementation, in
addition to final remarks in order to create the presentation.

### Origin

After writing the iterative solution, which is of complexity O(n!), we
thought of possible ways to improve it, or even put it all aside and come
up with something new. We spent a lot of time trying to come up with a
polynomial solution to the problem, or at least show that it is NP-hard.

One of those polynomial attempts was to seek a greedish path. Not only
greedy in terms of finding the smallest or largest delay, but rather two
greedy policies that can be switched up during runtime.

The algorithm will, like binary search, attempt to find a possible path
which is closest to the threshold. The tool it will use to switch up or
down will be the ratio of jumps it takes with a maximizing greedy method to
the jumps it takes with a minimizing greedy method, the algorithm partially
worked, but failed in many cases. After further investigation of the
possible permutations that this approach won't be able to cover we
abandoned it.

Later on, we sought a path in which we can combine this approach with the
dynamic programming main algorithm we found to fasten the algorithm on the
cost of lower accuracy.

### Idea

The main idea revolves around the following:

1. pick up a promising permutation
2. run the cached (db) giggle on the last log(n) databases in that permutation.
3. return the best result

The idea here is to pick a permutation which, by changing the log(n) end of
it we might be able to improve it sufficiently as to get the correct
answer, or something near it. The greedy algorithm comes in handy here, as
it allows us to find many "candidate" permutations that have values close
to the threshold quite quickly (in polynomial time). Then we can run giggle
on the log(n) ending databases in those permutations in an attempt to
improve the results and get them closer to the correct answer.

### Quick results on the given input set

```
giggle0:

real 0m0.037s
user 0m0.007s
sys 0m0.013s

giggle (cached):
real    0m3.386s
user    0m3.246s
sys 0m0.137s

giggle2 (cached):
real    0m6.823s
user    0m6.455s
sys 0m0.363s

iterative (brute force):
real    0m20.544s
user    0m19.619s
sys 0m0.913

hybrid (approximation): (around 25/100 were close, and 75/100 were correct)
real    0m0.204s
user    0m0.193s
sys 0m0.011s
```

```
; 1240496/19663005
	~0.06308781389212889891
```

We will continue to invisitage the algorithmic complexity of our approach, and
find an explination for why memoization helped. Initially it seems since
our problem is very similar to TSP, our solution might have a similar
complexity to the TSP dynamic programming solution which is O(2^n * n^2).


