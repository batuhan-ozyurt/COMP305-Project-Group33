#!/usr/bin/env python

import argparse
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

    parser = argparse.ArgumentParser(description='Giggle Algorithms Runner')
    parser.add_argument('-m', '--method', type=str, default="giggle", required=False, help="name of the method to use: giggle, giggle2, iterative, hybrid")
    parser.add_argument('-b', '--base', type=float, default=2, required=False, help="the log base to use if hybrid was picked")
    parser.add_argument('-i', '--input', type=str, required=True, help="the path to the input file")
    args = parser.parse_args()

    input = open(args.input)


    numtests = int(input.readline())

    for i in range(numtests):
        input.readline() # number of elements
        arrstr = input.readline().strip().split(" ")
        arr = list(map(lambda x : int(x), arrstr))
        timeout = int(input.readline()) # line with timeout

        result = -1

        if args.method == "giggle":
            result = giggle.giggle(arr, timeout)
        elif args.method == "giggle2":
            result = giggle2.giggle2(arr, timeout)
        elif args.method == "iterative":
            result = iterative.giggleiter(arr, timeout)
        elif args.method == "hybrid":
            result = hybrid.gigglehybrid(arr, timeout, args.base)
        else:
            print("Invalid method.")
            print("Valid methods are: giggle, giggle2, iterative, hybrid.")
            return


        if result == -1:
            result = "NO SOLUTION"

        print("Case #{}: {}".format(i + 1, result))


if __name__ == "__main__":
    main()
