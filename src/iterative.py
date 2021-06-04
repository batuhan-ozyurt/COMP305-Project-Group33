import itertools

def giggleiter(dbs, timeout):

    # Make sure the source is not present within the db list as it is not
    # required for finding all possible paths (since it is known to be the source and the destination)

    dbsl = list(dbs)
    dbsl.remove(0)
    dbs = tuple(dbsl)


    sums = [-1]

    # loop over all possible permutations, and collect their path's sum in the sums array
    for perm in itertools.permutations(dbs):
        count = 0
        prev = 0

        for db in perm:
            count += abs(prev - db)
            prev = db

            # if we bypass the timeout, stop
            if count > timeout:
                break

        count += abs(prev - 0)

        if count > timeout:
            continue

        print(perm, count)
        sums.append(count)

    return max(sums)
