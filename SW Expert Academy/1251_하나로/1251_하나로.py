import heapq

def prim(start):
    total = 0

    key[start] = 0
    heapq.heappush(pq, (key[start], 0))

    while pq:
        dis, u = heapq.heappop(pq)
        if visit[u] : continue
        visit[u] = 1
        total += dist[p[u]][u] * E

        for v in range(N):
            if visit[v] == 0 and key[v] > dist[u][v]:
                key[v] = dist[u][v]
                p[v] = u
                heapq.heappush(pq, (key[v], v))
    return total

T = int(input())
for t in range(1, T+1):
    N = int(input())
    key = [float('inf')] * N
    visit = [0] * N
    p = list(range(N))
    pq = []

    x_s = list(map(int, input().split()))
    y_s = list(map(int, input().split()))
    E = float(input())

    dist = [[0]*N for _ in range(N)]
    for i in range(N-1):
        for j in range(i+1, N):
            dist[i][j] = dist[j][i] = (x_s[i]-x_s[j])**2 + (y_s[i]-y_s[j])**2

    print('#{} {}'.format(t, round(prim(0))))




