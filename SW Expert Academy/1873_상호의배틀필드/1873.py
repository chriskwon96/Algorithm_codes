T = int(input())
# .: plain, *: 벽돌, #: 강철, _: 물,
di = [-1, +1, 0, 0] # u d l r
dj = [0, 0, -1, +1]
arr = ['^', 'v', '<', '>']

for t in range(1, T+1):
    H, W = map(int, input().split())
    matrix = [list(input()) for _ in range(H)]
    N = int(input())
    moves = list(input())

    for i in range(H):
        for j in range(W):
            if matrix[i][j] in arr:
                r, c = i, j # 함선의 좌표


    for i in range(len(moves)):
        command = moves[i]
        if command == 'S':
            now_di = di[arr.index(matrix[r][c])] # 현재방향
            now_dj = dj[arr.index(matrix[r][c])]
            rr = r + now_di
            cc = c + now_dj

            while (0<=rr < H) and (0<=cc < W):

                if matrix[rr][cc] in ['*', '#']: # 다음꺼가 벽돌이나 강철이면
                    if matrix[rr][cc] == '*': #벽돌이면
                        matrix[rr][cc] = '.' #평지로 바꿔라
                        break
                    else: #강철이면
                        break
                else: #벽돌이나 강철이 아니면
                    rr += now_di
                    cc += now_dj # 한칸 전진


        else:
            if command == 'U':
                k = 0
            if command == 'D':
                k = 1
            if command == 'L':
                k = 2
            if command == 'R':
                k = 3

            matrix[r][c] = arr[k]  # 모양바꾸고
            if (0<=r+di[k]<H) and (0<=c+dj[k] < W): #다음칸이 존재한다면
                if matrix[r+di[k]][c+dj[k]] == '.': #다음칸이 평지라면
                    matrix[r+di[k]][c+dj[k]], matrix[r][c] = matrix[r][c], matrix[r+di[k]][c+dj[k]]
                    r = r +di[k]
                    c = c + dj[k]


    print('#{}'.format(t),end = ' ')
    for row in matrix:
        print(''.join(row))
