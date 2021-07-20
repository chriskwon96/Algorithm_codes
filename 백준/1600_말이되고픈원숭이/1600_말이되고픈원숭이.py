from collections import deque


di1 = [0, -1, 0, +1]
dj1 = [+1, 0, -1, 0]
di2 = [+1, -1, -2, -2, +1, -1, +2, +2]
dj2 = [+2, +2, +1, -1, -2, -2, +1, -1]

def bfs():
    q.append([0,0,0])
    check[0][0][0] = 1
    while q:
        x,y,h = q.popleft()
        if x==H-1 and y==W-1:
            print(check[x][y][h]-1)
            return
        else:
            if h < K:

                monkey(x,y,h)
                horse(x, y, h)
            else:
                monkey(x,y,h)
    print(-1)

def monkey(x,y,h):
    for k in range(4):
        nx, ny = x+di1[k], y+dj1[k]
        if 0<=nx<H and 0<=ny<W:
            if matrix[nx][ny] == 0 and check[nx][ny][h] == 0:
                check[nx][ny][h] = check[x][y][h] + 1
                q.append([nx, ny, h])

def horse(x,y,h):
    for k in range(8):
        nx, ny = x+di2[k], y+dj2[k]
        if 0<=nx<H and 0<=ny<W:
            if matrix[nx][ny] == 0 and check[nx][ny][h+1] == 0:
                check[nx][ny][h+1] = check[x][y][h] + 1
                q.append([nx,ny,h+1])

K = int(input())
W, H = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(H)]
check = [[[0]*(K+1) for _ in range(W)] for _ in range(H)]
q = deque()

bfs()

