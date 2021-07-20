from collections import deque


dirs=[(0, +1), (-1,0), (0,-1), (+1, 0)]


def bfs(q):

    while q:
        x,y,d = q.popleft()
        for k in range(4):
            nx, ny = x+dirs[k][0], y+dirs[k][1]
            if 0<=nx<N and 0<=ny<M and matrix[nx][ny] != -1 and not checked[nx][ny]:
                checked[nx][ny] = 1
                q.append((nx,ny,d+1))
    return d



M, N = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
checked = [[0]*M for _ in range(N)]

flag = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            flag = 1
            break
    if flag: break

if not flag:
    print(flag)
else:
    q = deque()
    for i in range(N):
         for j in range(M):
             if matrix[i][j] == 1:
                 q.append((i,j,0))
                 checked[i][j] = 1
    d = bfs(q)
    imposs = 0
    for i in range(N):
        for j in range(M):
            if checked[i][j] == 0 and matrix[i][j] == 0:
                imposs = 1
                print(-1)
                break
        if imposs: break
    if not imposs: print(d)



