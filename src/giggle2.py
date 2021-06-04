from functools import cache

@cache
def gigglehelper2(dbs, timeout, prevhob):
    ldbs = list(dbs)

    if len(ldbs) == 1:
        if ldbs[0] <= timeout:
            return list([abs(prevhob)])
        else:
            return list([-1])

    resarr = [-1]

    for node in dbs:
        if node == 0:
            continue

        dbscurr = ldbs.copy()
        dbscurr.remove(node)
        result = gigglehelper2(tuple(dbscurr), timeout, node)

        for path in result:
            if path == -1:
                continue

            if path + abs(prevhob - node) > timeout:
                continue

            resarr.append(abs(prevhob - node) + path)


    return resarr

def giggle2(dbs, timeout):
    return max(gigglehelper2(tuple(dbs), timeout, 0))
