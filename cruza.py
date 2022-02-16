import random


def _repeated(element, collection):
    c = 0
    for e in collection:
        if e == element:
            c += 1
    return c > 1
 
def _swap(data_a, data_b, cross_points):
    c1, c2 = cross_points
    new_a = data_a[:c1] + data_b[c1:c2] + data_a[c2:]
    new_b = data_b[:c1] + data_a[c1:c2] + data_b[c2:]
    return new_a, new_b
 
 
def _map(swapped, cross_points):
    n = len(swapped[0])
    c1, c2 = cross_points
    s1, s2 = swapped
    map = s1[c1:c2], s2[c1:c2]
    for i_chromosome in range(n):
        if not c1 < i_chromosome < c2:
            for i_son in range(2):
                while _repeated(swapped[i_son][i_chromosome], swapped[i_son]):
                    mapindex = map[i_son].index(swapped[i_son][i_chromosome])
                    swapped[i_son][i_chromosome] = map[1-i_son][mapindex]
    return s1, s2
 
 
def pmx(parent_a, parent_b):
    assert(len(parent_a) == len(parent_b))
    crosspoints = sorted([random.randint(1, len(parent_a)) for i in range(2)])
    swapped = _swap(parent_a, parent_b, crosspoints)
    mapped = _map(swapped, crosspoints)
 
    return mapped

