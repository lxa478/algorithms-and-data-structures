data = []
size = []

def find(i):
    while i != data[i]:
        data[i] = data[data[i]]
        i = data[i]
    return i
    
    if i != data[i]:
        data[i] = find(data[i])
    return data[i]

def union(i, j):
    pi, pj = find(i), find(j)
    if size[pi] < size[pj]:
        data[pi] = pj
        size[pj] += size[pi]
    else:
        data[pj] = pi
        size[pi] += size[pj]

def connected(i, j):
    return find(i) == find(j)