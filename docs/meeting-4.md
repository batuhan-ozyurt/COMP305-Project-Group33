# Summary (Meeting, 2021-06-04)

In this meeting we will discuss the newly added "hybrid" implementation, in
addition to final remarks in order to create the presentation.

## Origin

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

## Idea

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

## Quick results on the given input set

```
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
