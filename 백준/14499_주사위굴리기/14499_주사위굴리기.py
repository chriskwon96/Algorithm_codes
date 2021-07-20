di = [0, 0, -1, +1]
dj = [+1, -1, 0, 0]

def roll(dice, dir):
    if dir == 1: #right
        dice[0], dice[1], dice[3], dice[5] = dice[1], dice[5], dice[0], dice[3]
    elif dir == 2: #left
        dice[0], dice[1], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[1]
    elif dir == 3: #north
        dice[0], dice[2], dice[4], dice[5] = dice[2], dice[5], dice[0], dice[4]
    else: #south
        dice[0], dice[2], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[2]


N, M, x, y, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
dirs = list(map(int, input().split()))
dice = [0]*6
nx, ny = x,y
for dir in dirs:
    nx, ny = nx+di[dir-1], ny+dj[dir-1]
    if 0<=nx<N and 0<=ny<M: #범위안에 있다면
        roll(dice, dir)
        if matrix[nx][ny] == 0:
            matrix[nx][ny] = dice[0]
        else:
            dice[0] = matrix[nx][ny]
            matrix[nx][ny] = 0
        print(dice[5])
    else:
        nx, ny = nx-di[dir-1], ny-dj[dir-1]
