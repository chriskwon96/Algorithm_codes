N = int(input()) #정점의 개수
matrix = [list(map(int, input().split())) for _ in range(N)] #인접행렬
result = [[0]*N for _ in range(N)]

def dfs(i, j):
    stack.append(i)
    while stack:
        start = stack.pop()
        for k in range(N):
            if matrix[start][k] == 1 and k not in visited:
                stack.append(k)
                visited.append(k)
                if j in visited:
                    return 1
    return 0

for i in range(N):
    for j in range(N):
        stack = []
        visited = []

        result[i][j] = dfs(i, j)
for row in result:
    print(' '.join(map(str, row)))
