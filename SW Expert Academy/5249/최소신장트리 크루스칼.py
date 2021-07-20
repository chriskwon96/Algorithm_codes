def find_set(x):
    if p[x] == x:
        return x
    else:
        return find_set(p[x])

def union(u,v):
    pu = find_set(u)
    p[v] = pu

tc= int(input())
for t in range(tc):
    V, E = map(int, input().split())
    G = [list(map(int, input().split())) for _ in range(E)]

    p = list(range(V+1))

    total = 0
    cnt = 0

    G.sort(key=lambda x: x[2])

    while cnt < V:
        u,v,val = G.pop(0)
        if find_set(u) != find_set(v):
            union(u,v)
            cnt += 1
            total += val

    print("#{} {}".format(t+1, total))





