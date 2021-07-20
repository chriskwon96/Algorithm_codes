import sys
sys.setrecursionlimit(10**7)

dirs = [(0, +1), (-1, 0), (0, -1), (+1,0)]


def dfs(x,y, height):
    global routes
    if x==N-1 and y == M-1:
        return 1
    routes = 0
    for k in range(4):
        nx, ny = x + dirs[k][0], y + dirs[k][1]
        if 0<= nx <N and 0<= ny <M and height > matrix[nx][ny]:
            if visited[nx][ny] != -1:
                routes += visited[nx][ny]
            else:
                routes += dfs(nx,ny,matrix[nx][ny])

    visited[x][y] = routes
    return routes

N,M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]


print(dfs(0,0,matrix[0][0]))
