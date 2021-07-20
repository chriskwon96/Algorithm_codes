dirs = [(0, +1), (-1, 0), (0, -1), (+1, 0)]

def bfs(start):
    q = [start]
    while q:
        x,y,d = q.pop(0)
        for k in range(4):
            nx, ny = x+dirs[k][0], y+dirs[k][1]
            if 0<=nx<N and 0<=ny<M and matrix[nx][ny] == 1 and checked[nx][ny] == 0:
                if nx == N-1 and ny == M-1:
                    return d+1
                q.append((nx,ny,d+1))
                checked[nx][ny] = 1


N, M = map(int, input().split())

matrix = [list(map(int, input())) for _ in range(N)]
checked=[[0]*M for _ in range(N)]
checked[0][0] = 1

print(bfs((0,0,1)))

