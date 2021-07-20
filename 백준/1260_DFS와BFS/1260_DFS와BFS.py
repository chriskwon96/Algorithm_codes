def dfs(start):
    print(start+1, end = " ")
    for i in range(N):
        if matrix[i][start] and v[i] == 0:
            v[i] = 1
            dfs(i)

def bfs(start):
    q = [start]
    while q:
        head = q.pop(0)
        print(head+1, end=" ")
        for i in range(N):
            if matrix[i][head] and v[i] == 0:
                v[i] = 1
                q.append(i)




N, M, V = map(int, input().split())

matrix = [[0]*N for _ in range(N)]

for _ in range(M):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    matrix[i][j], matrix[j][i] = 1, 1

v = [0]*N
v[V-1] = 1
dfs(V-1)
print()
v = [0]*N
v[V-1] = 1
bfs(V-1)
