# from http://stackoverflow.com/questions/18721774/python-cluster-variables-in-list-of-tuples-by-2-factors-silmutanously
def stat(lst, index):
    """Calculate mean and std deviation from the input list."""
    n = float(len(lst))
    mean = sum([pair[index] for pair in lst])/n
    stdev = sqrt((sum(x[index]*x[index] for x in lst) / n) - (mean * mean))
    return mean, stdev

def parse(lst, n, index):
    cluster = []
    for i in lst:
        if len(cluster) <= 1:    # the first two values are going directly in
            cluster.append(i)
            continue
        mean, stdev = stat(cluster, index)
        if (abs(mean - i[index]) > n * stdev):   # check the "distance"
            yield cluster
            cluster[:] = []    # reset cluster to the empty list

        cluster.append(i)
    yield cluster           # yield the last cluster

for cluster in parse(array, 7, 0):
    for nc in parse(cluster, 3, 2):
        print nc

[(1, 'a', 10), (2, 'a', 11)]
[(3, 'c', 200)]
[(60, 'a', 12), (70, 't', 13)]
[(80, 'g', 300), (100, 'a', 305)]
[(220, 'c', 307), (230, 't', 306)]
[(250, 'g', 302)]
