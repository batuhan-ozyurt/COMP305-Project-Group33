#!/usr/bin/env python


"""

DBS: [0, ... ] (N many dbs)
TIMEOUT: K (maximum acceptable delay)
PREVHOP: The hop which we traveled from
CURRTIME: The accumulating time (to check against timeout)
INDX: The INDX of the next hop (DB) to jump to.

1. Pick element from DBS
2. Sum |current element - picked elemenet| with current time.
3. if sum > timeout then return none
4. remove selected element from DBS
5. run DBS.length times the algo on new DBS and supply calculated time sum.
6. return the one with maximum return value

"""


def gigglehelper(dbs, timeout, prevhob, currtime, indx):
    dbs = dbs.copy()

    # If now is the time to jump back to 0 do it.
    if len(dbs) <= 1:
        if  currtime + abs(0 - prevhob ) <= timeout:
            return  currtime + abs(0 - prevhob)
        return -1

    # get hold of the next db to jump to and add the jumps time to the current time
    nexthop = dbs.pop(indx)
    newtime = currtime + abs(nexthop - prevhob)

    # make sure we did not pass the timeout threshold yet
    if newtime > timeout:
        return -1

    # run on possible paths and accumulate their results in an array
    res = []
    for i in range(len(dbs)):

        # do not jump to 0 if we are not at the last jump yet
        if dbs[i] == 0 and len(dbs) > 1:
            continue

        res.append(gigglehelper(dbs, timeout, nexthop, newtime, i))

    return max(res)


def giggle(dbs, timeout):
    return gigglehelper(dbs, timeout, 0, 0, len(dbs) - 1)



def main():

    input = open("input.txt")

    numtests = int(input.readline())

    for i in range(numtests):
        input.readline() # number of elements
        arrstr = input.readline().strip().split(" ")
        arr = list(map(lambda x : int(x), arrstr))
        timeout = int(input.readline()) # line with timeout
        result = giggle(arr,timeout)

        if result == -1:
            result = "NO SOLUTION"

        print("CASE {}: {}".format(i + 1, result))


if __name__ == "__main__":
    main()
