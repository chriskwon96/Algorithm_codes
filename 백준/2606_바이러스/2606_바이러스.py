def bfs(start):
    global ans
    q = [start]
    while q :
        head = q.pop(0)
        for i in range(N+1):
            if matrix[i][head] and v[i] == 0:
                v[i] = 1
                ans += 1
                q.append(i)


N = int(input())
V = int(input())
matrix = [[0]*(N+1) for _ in range(N+1)]

for _ in range(V):
    i,j = map(int, input().split())
    matrix[i][j], matrix[j][i] = 1, 1

ans = 0
v = [0]*(N+1)
v[1] = 1

bfs(1)

print(ans)

