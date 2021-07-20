board = [[1,2,0]]

i=0
N=3
for n in range(N - 1, 0, -1):
    if board[i][n] == 0:
        for m in range(n - 1, -1, -1):
            if board[i][m]:  # 0이 아닌애를 발견하면
                print(n,m)
                board[i][n], board[i][m] = board[i][m], board[i][n]  # swap
print(board)