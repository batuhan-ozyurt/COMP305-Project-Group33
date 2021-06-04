#!/usr/bin/env python

import giggle
import giggle2
import iterative
import hybrid

"""
Main giggle algorithm (Dynamic programming)

DBS: [0, ... ] (N many dbs)
TIMEOUT: K (maximum acceptable delay)
PREVHOP: The hop which we traveled from
CURRTIME: The accumulating time (to check against timeout)
INDX: The INDX of the next hop (DB) to jump to.

0. memoize all
1. Pick element from DBS
2. Sum |current element - picked elemenet| with current time.
3. if sum > timeout then return none
4. remove selected element from DBS
5. run DBS.length times the algo on new DBS and supply calculated time sum.
6. return the one with maximum return value

"""


def main():

    input = open("input.txt")

    numtests = int(input.readline())

    for i in range(numtests):
        input.readline() # number of elements
        arrstr = input.readline().strip().split(" ")
        arr = list(map(lambda x : int(x), arrstr))
        timeout = int(input.readline()) # line with timeout

        result = giggle.giggle(arr, timeout)
        # result = giggle2.giggle2(arr, timeout)
        # result = iterative.giggleiter(arr, timeout)
        # result = hybrid.gigglehybrid(arr, timeout, 2)

        if result == -1:
            result = "NO SOLUTION"

        print("Case #{}: {}".format(i + 1, result))


if __name__ == "__main__":
    main()
