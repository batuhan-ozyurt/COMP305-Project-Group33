from math import floor, log
from giggle import gigglehelper

def attempt(dbs, maxjumps, startleft):
    lindx, rindx = 0, len(dbs) - 1

    left = startleft

    count = 0
    prevhop = dbs.index(0)
    nojumps = 0

    jumps = [0]

    if dbs[lindx] == 0:
        left = False

    if dbs[rindx] == 0:
        left = True

    while (lindx != rindx):
        if nojumps >= maxjumps:
             left != left
             break

        nojumps += 1
        if left:
            count += abs(dbs[prevhop] - dbs[lindx])
            prevhop = lindx
            lindx += 1
            if dbs[rindx] != 0:
                left = False
        else:
            count += abs(dbs[prevhop] - dbs[rindx])
            prevhop = rindx
            rindx -= 1
            if dbs[lindx] != 0:
                left = True

        jumps.append(dbs[prevhop])

    if dbs[lindx] == 0:
        left = False

    if dbs[rindx] == 0:
        left = True

    while (lindx != rindx):
        if left:
            count += abs(dbs[prevhop] - dbs[lindx])
            prevhop = lindx
            lindx += 1
            if dbs[lindx] == 0:
                left = False
        else:
            count += abs(dbs[prevhop] - dbs[rindx])
            prevhop = rindx
            rindx -= 1
            prevhop = rindx + 1
            if dbs[rindx] == 0:
                left = True
        jumps.append(dbs[prevhop])

    count += abs(dbs[prevhop] - dbs[dbs.index(0)])

    return count, jumps

def checktimeout(dbs, timeout):
    dbs.sort()

    lres = attempt(dbs, 0, True)
    rres = attempt(dbs, 0, False)

    if min(lres[0], rres[0]) <= timeout:
        return True
    else:
        return False

def findclose(dbs, timeout, startleft):
    left, right = 0, len(dbs)

    lastmax = []
    lastmin = []

    while left != right:
        res, path = attempt(dbs, (left+right)/2, startleft)

        if res > timeout:
            right -= 1
            lastmax = (res, path)
            continue

        if res < timeout:
            left += 1
            lastmin = (res, path)
            continue

        if res == timeout:
            left = 0
            right = 0

            lastmin = (res, path)
            lastmax = (res, path)

    return lastmin, lastmax

def continuegiggle(dbs, dbsleft, timeout):
    currtime = 0
    prev = 0
    for i in range(len(dbs)):
        if i == 0:
            continue

        currtime += abs(prev - dbs[i])
        prev = dbs[i]


    res = [-1]

    dbsleft.append(0)
    for i in range(len(dbsleft)):
        if dbsleft[i] == 0 and len(dbsleft) > 1:
            continue

        res.append(gigglehelper(tuple(dbsleft), timeout, dbs[-1], currtime, i))

    return max(res)

#
# print(lclosepaths[0][1])
# print(lclosepaths[1][1])
# print(rclosepaths[1][1])
# print(rclosepaths[0][1])
# localdbs = rclosepaths[0][1][:len(dbs)-3]
# localdbsleft = rclosepaths[0][1][len(dbs)-3:]
# print(localdbs)
# print(localdbsleft)
# print(continuegiggle(localdbs, localdbsleft, timeout))

def gigglehybrid(dbs, timeout, base):
    if not checktimeout(dbs, timeout):
        return -1

    dbs.sort()

    lclosepaths = findclose(dbs, timeout, True)
    rclosepaths = findclose(dbs, timeout, False)

    minlres = attempt(dbs, 0, True)
    minrres = attempt(dbs, 0, False)
    maxlres = attempt(dbs, len(dbs), False)
    maxrres = attempt(dbs, len(dbs), True)

    res = []

    if maxlres[0] <= timeout:
        res.append(maxlres[0])

    if maxrres[0] <= timeout:
        res.append(maxrres[0])

    if minlres[0] <= timeout:
        res.append(minlres[0])

    if minrres[0] <= timeout:
        res.append(minrres[0])


    if len(lclosepaths[0]) > 0 and lclosepaths[0][0] <= timeout:
        res.append(lclosepaths[0][0])

    if len(lclosepaths[1]) > 0 and lclosepaths[1][0] <= timeout:
        res.append(lclosepaths[1][0])

    if len(rclosepaths[0]) > 0 and rclosepaths[0][0] <= timeout:
        res.append(rclosepaths[0][0])

    if len(rclosepaths[1]) > 0 and rclosepaths[1][0] <= timeout:
        res.append(rclosepaths[1][0])


    for i in range(len(dbs)):
        if len(lclosepaths[0]) > 0:
            localdbs = lclosepaths[0][1][:len(dbs)-i]
            localdbsleft = lclosepaths[0][1][len(dbs)-i:]
            res.append(continuegiggle(localdbs, localdbsleft, timeout))

        if len(lclosepaths[1]) > 0:
            localdbs = lclosepaths[1][1][:len(dbs)-i]
            localdbsleft = lclosepaths[1][1][len(dbs)-i:]
            res.append(continuegiggle(localdbs, localdbsleft, timeout))

        if len(rclosepaths[0]) > 0:
            localdbs = rclosepaths[0][1][:len(dbs)-i]
            localdbsleft = rclosepaths[0][1][len(dbs)-i:]
            res.append(continuegiggle(localdbs, localdbsleft, timeout))

        if len(rclosepaths[1]) > 0:
            localdbs = rclosepaths[1][1][:len(dbs)-i]
            localdbsleft = rclosepaths[1][1][len(dbs)-i:]
            res.append(continuegiggle(localdbs, localdbsleft, timeout))

        if i == floor(log(len(dbs), base)):
            break


    return max(res)
