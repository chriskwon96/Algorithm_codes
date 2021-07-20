
def find_set(x):
    if p[x] == x:
        return x
    else:
        return find_set(p[x])

def union(x,y):
    px, py = find_set(x), find_set(y)
    if rank[px] > rank[py]:
        p[py] = px
    else:
        p[px] = py
        if rank[px] == rank[py]:
            rank[py] += 1

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    pair = list(map(int, input().split()))
    p = [i for i in range(N+1)]
    rank = [0]*(N+1)
    cnt = 0
    for j in range(M):
        union(pair[2*j], pair[2*j+1])
    for k in range(N+1):
        if p[k] == k:
            cnt += 1

    print('#{} {}'.format(t, cnt-1))
