
# 프림

tc = int(input())
for t in range(tc):
    V, E = map(int, input().split())
    matrix = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        s,e,w = map(int, input().split())
        matrix[s][e] = w
        matrix[e][s] = w

    INF = float('inf')
    key = [INF]*(V+1)

    mst = [0]*(V+1)
    key[0] = 0
    cnt = 0
    total = 0

    while cnt < V+1:
        min_w = INF
        u = -1
        for i in range(V+1):
            if not mst[i] and key[i] < min_w:
                u = i
                min_w = key[i]
        mst[u] = 1
        total += min_w
        for v in range(V+1):
            if matrix[u][v] and not mst[v] and matrix[u][v] < key[v]:
                key[v] = matrix[u][v]
        cnt += 1

    print("#{} {}".format(t+1, total))







