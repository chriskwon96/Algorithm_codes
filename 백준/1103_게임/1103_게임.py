di = [0, -1, 0, +1]
dj = [+1, 0, -1, 0]

def move(x,y, val, turns):
    global max_turns

    for k in range(4):
        if dir_matrix[x][y][k] :
        nx, ny = x+val*di[k], y+val*dj[k]
        if 0<= nx <N and 0<= ny <M and matrix[nx][ny] != "H":
            if check[nx][ny]: #cycle이 만들어진다면
                max_turns = -1
                return
            else:
                check[nx][ny] = turns
                move(nx, ny, int(matrix[nx][ny]), turns+1)
                if max_turns == -1:
                    return
                check[nx][ny] = 0
        else:
            if turns > max_turns:
                max_turns = turns


N, M = map(int, input().split())

matrix = [list(input()) for _ in range(N)]
dir_matrix = [[[1,1,1,1] for _ in range(M)] for _ in range(N)]
check = [[0]*M for _ in range(N)]


max_turns = 0
move(0, 0, int(matrix[0][0]), 0)
print(max_turns)





