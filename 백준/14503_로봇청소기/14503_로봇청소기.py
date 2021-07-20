di = [-1, 0, +1, 0] #N E S W clockwise
dj = [0, +1, 0, -1]

N, M = map(int, input().split())
r, c, d = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
cnt = 1
flag = 4
matrix[r][c] = 2
nr, nc, h = r, c, d

while flag:
    h = h - 1
    if h < 0 :
        h = 3
    nr = nr + di[h] #왼쪽으로 회전후 전진
    nc = nc + dj[h]

    #왼쪽 방향 체크
    if 0 < nr < N and 0 < nc < M:
        if matrix[nr][nc] == 0:
            matrix[nr][nc] = 2 #청소해라
            cnt += 1
            flag = 4

        else:
            # 청소할 수 없다면
            nr = nr - di[h]
            nc = nc - dj[h]  # 원상복귀
            flag -= 1
    else:
        # 벽이라면
        nr = nr - di[h]
        nc = nc - dj[h]  # 원상복귀
        flag -= 1

    if flag == 0:
    #네 방향모두 청소가 되어있거나 벽인 경우
        nr = nr + di[(h+2) % 4]
        nc = nc + dj[(h+2) % 4]
        if 0 < nr < N and 0 < nc < M and matrix[nr][nc] != 1:
            flag = 4
        else:
            break



print(cnt)