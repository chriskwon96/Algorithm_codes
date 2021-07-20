def dfs(i):
    # print(v)
    v[i] = 1
    for j in range(1, N+1):
        if matrix[i][j] == 1 and v[j] == 0 :
            dfs(j)

N, M = map(int, input().split())
matrix = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    u,v = map(int, input().split())
    matrix[u][v], matrix[v][u] = 1,1

v = [0]*(N+1)
cnt = 0
for x in range(1, N+1):
    # print(v)
    if v[x] == 0:
        # print(v)
        cnt += 1
        dfs(x)

print(cnt)





