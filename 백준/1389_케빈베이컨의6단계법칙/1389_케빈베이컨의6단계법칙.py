def dfs(i, j): #i에서 j로의 최단거리
    stack.append(i)
    visited[i] = 1
    paths = []
    while stack:
        start = stack.pop()
        n = visited[start] + 1
        for k in range(N):
            if matrix[start][k] == 1 and visited[k] == 0:
                stack.append(k)
                visited[k] = n
                if k == j:
                    paths.append(n)

    return (sum(visited) - N)

N, M = map(int, input().split())
matrix = [[0]*N for _ in range(N)]
for _ in range(M):
    i, j = map(int, input().split())
    i = i-1
    j = j-1
    matrix[i][j] = 1
    matrix[j][i] = 1

bacon = [0] * N # 모든 사람의 베이컨 수

for i in range(N):
    for j in range(N):
        stack = []
        visited = [0]*N
        bacon[i] = dfs(i, j)

for i in range(N):
    if bacon[i] == min(bacon):
        print(i)
print(bacon.index(min(bacon))+1)
