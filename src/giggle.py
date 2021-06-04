from functools import cache

@cache
def gigglehelper(dbs, timeout, prevhob, currtime, indx):
    # print("==", "dbs:", dbs, "timeout:", timeout, "prevhob:", prevhob, "currtime:", currtime, "indx:", indx, "==")
    # print("==", "dbs:", dbs, "==")

    dbsl = list(dbs)

    # get hold of the next db to jump to and add the jumps time to the current time
    nexthop = dbsl.pop(indx)
    newtime = currtime + abs(prevhob - nexthop)

    dbs = tuple(dbsl)

    # If now is the time to jump back to 0 do it.
    if len(dbs) == 0 and newtime <= timeout:
        return newtime

    # make sure we did not pass the timeout threshold yet
    if newtime > timeout:
        return -1

    # run on possible paths and accumulate their results in an array
    res = [-1]
    for i in range(len(dbs)):

        # do not jump to 0 if we are not at the last jump yet
        if dbs[i] == 0 and len(dbs) > 1:
            continue

        res.append(gigglehelper(dbs, timeout, nexthop, newtime, i))

    return max(res)


def giggle(dbs, timeout):
    res = []

    for i in range(len(dbs)):
        if dbs[i] == 0 and len(dbs) > 1:
            continue

        res.append(gigglehelper(tuple(dbs), timeout, 0, 0, i))

    return max(res)
