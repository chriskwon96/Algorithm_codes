from collections import deque

global escape
di = [0, -1, 0, +1]
dj = [+1, 0, -1, 0]



def dfs(x,y,d):
    global min_d, escape

    if d+1 == min_d:
        return


    for k in range(4):
        nx, ny = x+di[k], y+dj[k]
        if 0<=nx<N and 0<=ny<M:

            if matrix[nx][ny] == '.':
                dfs(nx,ny,d+1)

            elif matrix[nx][ny].isalpha():
                if matrix[nx][ny].lower() == matrix[nx][ny]:
                    mykeys.add(matrix[nx][ny])
                    dfs(nx,ny,d+1)
                else:
                    if matrix[nx][ny].lower() in mykeys:
                        # check[nx][ny] = 1
                        # q.append((nx,ny,d+1))
                        dfs(nx, ny, d+1)

            elif matrix[nx][ny] == '1':
                escape = d+1
                break
        if escape > -1:
            break
    if escape > -1:
        min_d = escape








N, M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]

# for m in matrix: print(m)

mykeys=set()
min_d = N*M + 1


for i in range(N):
    for j in range(M):
        if matrix[i][j] == "0":

            escape = -1
            dfs(i,j,0)

if min_d == N*M+1:
    print(-1)
else:
    print(min_d)
