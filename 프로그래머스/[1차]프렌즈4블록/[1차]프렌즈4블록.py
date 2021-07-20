




def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])
    blocks = 0
    flag = 1
    while flag: #지워지는 블럭이 있다면 반복

        check = [[0]*n for _ in range(m)]
        flag = 0

        for i in range(m-1): # 모든 네모에 대해 검사
            for j in range(n-1):
                me = board[i][j]
                if me == board[i+1][j] == board[i][j+1] == board[i+1][j+1] and me: #터질게 있다면
                    check[i][j] = check[i+1][j] = check[i][j+1] = check[i+1][j+1] = 1
                    flag = 1

        # 터지는 블럭세기
        for i in range(m):
            for j in range(n):
                if check[i][j]:
                    blocks += 1
                    board[i][j] = 0
        # print(board)
        # print('=================')

        # 아래로 내리기
        for j in range(n):
            zero = 0
            for i in range(m-1, -1, -1):
                if board[i][j] == 0:
                    zero += 1
                else:
                    if zero:
                        board[i+zero][j] = board[i][j]
                        board[i][j] = 0
        # print(board)


    return blocks









m,n = 4,5
board = ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']

solution(m, n, board)

