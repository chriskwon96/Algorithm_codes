di = [0, +1, 0, -1]
dj = [+1, 0, -1, 0]

def bfs():
    global min_dis
    while q:
        x, y = q.pop(0)
        dis = min_matrix[x][y] # [x,y]까지 도착하는데 걸린 지금까지의 최소거리
        for k in range(4):
            new_x, new_y = x + di[k], y + dj[k]
            if 0 <= new_x <= N-1 and 0 <= new_y <= N-1 and (new_x or new_y): # G에 도착 전
                if [new_x, new_y] == G:  # G에 도착
                    if dis < min_dis:  # G 새로운 최소 거리 갱신
                        min_dis = dis
                else:
                    if dis+matrix[new_x][new_y] < min_matrix[new_x][new_y]: #새로운 최소거리 갱신
                        min_matrix[new_x][new_y] = dis+matrix[new_x][new_y]
                        q.append([new_x, new_y])


T = int(input())
for t in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    min_dis = 100 * 100 * 10
    min_matrix = [[min_dis]*N for _ in range(N)]
    min_matrix[0][0] = 0
    S, G = [0, 0], [N-1, N-1]
    q = [S]
    bfs()
    print('#{} {}'.format(t, min_dis))



