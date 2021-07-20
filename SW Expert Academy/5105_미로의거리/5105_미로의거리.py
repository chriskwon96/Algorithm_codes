di = [-1, 0, +1, 0]
dj = [0, +1, 0, -1]

def bfs(S):
    queue.append(S)
    while queue:
        node = queue.pop(0)

        for k in range(4):
            x,y,z = node[0]+di[k], node[1]+dj[k], node[2]+1
            if 0<=x<N and 0<=y<N:
                if not matrix[x][y]: #0이면
                    if not visited[x][y]: #방문하지 않았다면
                        visited[x][y] = z #위치에 step값
                        queue.append([x,y,z])
                elif matrix[x][y] == 2:
                    return z-1
    return 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    matrix = [list(map(int,input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 3:
                S = [i,j,0] #3의 위치
                break
    visited = [[0]*N for _ in range(N)]
    queue = []
    print('#{} {}'.format(t, bfs(S)))

