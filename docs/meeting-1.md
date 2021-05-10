# Summary (Meeting, 2021-05-10)

We discussed the problem and discussed multiple possible
solutions, finding counter examples for some of those
solutions and agreeing continue investigating the other
solutions.

## First Idea (zig zag)

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

## Second Idea (zig zag from all)

1. Pick a database (other than zero) that was not started from previously.
2. from 0 jump to that database.
3. jump to lowest unvisited database.
4. jump to highest unvisited database.
5. if not at 0, go to step 3.
6. store the sum of all jumps.
7. go to step 1.
8. return the heights sum recorded.

## Third Idea (Scheduling meetings?)

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

## Fourth Idea (all possible paths)

1. from zero recurse by jumping to all other databases. 
2. recurse by jumping to all other unvisited databases. (maybe use dynamic programming to reduce complexity)
3. from all of the possible paths, return the one with highest value.


## Extra notes

We might have ignored the fact that we need to
find the longest response time **within a
threshold**, meaning that for the same database
array (input), changing the threshold can change the
correct answer (output).
