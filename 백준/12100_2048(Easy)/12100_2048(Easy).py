
from copy import deepcopy

di = [0, -1, 0, +1]
dj = [+1, 0, -1, 0]


def find_block(board, cur_max):
    for b in board:
        if cur_max < max(b):
            cur_max = max(b)
    return cur_max


def turn(board, di, dj):
    if dj>0:
        for i in range(N):
            u,v = 0,0
            while v < N-1:
                if board[i][u]:
                    while not board[i][v]:
                        v += 1
                    if board[i][u] == board[i][v]:
                        board[i][u] = board[i][u]*2
                        board[i][v] = 0
                    u, v = v+1, v+2
                else:
                    u += 1
                    v = u+1

            #shift
            for n in range(N - 1):
                if board[i][n] == 0:
                    for m in range(n + 1, N):
                        if board[i][m]:  # 0이 아닌애를 발견하면
                            board[i][n], board[i][m] = board[i][m], board[i][n]  # swap
                            break



    elif dj<0:
        for i in range(N):
            u, v = N-1, N-1
            while 0 < v:
                if board[i][u]:
                    while not board[i][v]:
                        v -= 1
                    if board[i][u] == board[i][v]:
                        board[i][u] = board[i][u] * 2
                        board[i][v] = 0
                    u, v = v - 1, v - 2
                else:
                    u -= 1
                    v = u - 1

            for n in range(N-1, 0, -1):
                if board[i][n] == 0:
                    for m in range(n-1, -1, -1):
                        if board[i][m]:  # 0이 아닌애를 발견하면
                            board[i][n], board[i][m] = board[i][m], board[i][n]  # swap
                            break



    elif di >0:
        for j in range(N):
            u, v = 0, 0
            while v < N - 1:
                if board[u][j]:
                    while not board[v][j]:
                        v += 1
                    if board[u][j] == board[v][j]:
                        board[u][j] = board[u][j] * 2
                        board[v][j] = 0
                    u, v = v + 1, v + 2
                else:
                    u += 1
                    v = u + 1
            for n in range(N - 1):
                if board[n][j] == 0:
                    for m in range(n + 1, N):
                        if board[m][j]:  # 0이 아닌애를 발견하면
                            board[n][j], board[m][j] = board[m][j], board[n][j]  # swap
                            break



    else:
        for j in range(N):
            u, v = N-1, N-1
            while 0 < v:
                if board[u][j]:
                    while not board[v][j]:
                        v -= 1
                    if board[u][j] == board[v][j]:
                        board[u][j] = board[u][j] * 2
                        board[v][j] = 0
                    u, v = v - 1, v - 2
                else:
                    u -= 1
                    v = u - 1

            for n in range(N-1, 0, -1):
                if board[n][j] == 0:
                    for m in range(n-1, -1, -1):
                        if board[m][j]:  # 0이 아닌애를 발견하면
                            board[n][j], board[m][j] = board[m][j], board[n][j]  # swap
                            break

    return board

def f(n, board):
    global cur_max

    if n == 5: #5번째 까지 돌렸다면
        cur_max = find_block(board, cur_max)
    else:
        for k in range(4):
            bboard = deepcopy(board)
            bboard = turn(bboard, di[k], dj[k])
            # print(board)
            # print(bboard, n, k)

            if board != bboard:
                f(n+1, bboard)
            else:
                cur_max = find_block(bboard, cur_max)



N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
cur_max = 0
f(0, matrix)
print(cur_max)


