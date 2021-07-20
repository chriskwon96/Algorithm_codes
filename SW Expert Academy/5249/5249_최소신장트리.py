T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1][n2], adj[n2][n1] = w, w
    INF = float('inf')
    key = [INF] * (V+1)

    mst = [False]*(V+1)

    key[0] = 0
    cnt = 0
    total = 0
    while cnt < (V+1):
        # 아직 mst가 아니고 key가 최소인 정점 u
        min_w = INF
        u = -1
        for i in range(V+1):
            if not mst[i] and key[i] < min_w:
                min_w = key[i]
                u = i
        # u를 mst에 추가
        mst[u] = True
        total += min_w
        # u에 인접하고 아직 mst가 아닌 정점 w에서 key[w] > u-w 가중치라면 key 갱신
        for v in range(V+1):
            if adj[u][v] > 0 and not mst[v] and key[v] > adj[u][v]:
                key[v] = adj[u][v]


        cnt += 1
    print('#{} {}'.format(t, total))




