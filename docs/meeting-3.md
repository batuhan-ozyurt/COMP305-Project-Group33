# Summary (Meeting, 2021-06-02)

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

```
; 1240496/19663005
	~0.06308781389212889891
```

We will continue to invisitage the algorithmic complexity of our approach, and
find an explination for why memoization helped. Initially it seems since
our problem is very similar to TSP, our solution might have a similar
complexity to the TSP dynamic programming solution which is O(2^n * n^2).
