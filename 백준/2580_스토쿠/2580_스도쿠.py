import sys

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
zeros = [] #0인 좌표찾기
for i in range(9):
    for j in range(9):
        if matrix[i][j] == 0:
            zeros.append([i,j])

def sudoku(coor, z):
    for k in range(1,10):
        if check(coor[0], coor[1], k): #가능한 후보라면
            matrix[coor[0]][coor[1]] = k #k를 넣고

            if z != (len(zeros)-1):
                sudoku(zeros[z + 1], z + 1)
                matrix[coor[0]][coor[1]] = 0  # reset
            else:
                for m in matrix:
                    print(' '.join(map(str, m)))
                sys.exit(0)




def check(i, j, k):

    #가로줄 세로줄 체크
    n = 0
    while n < 9:
        if matrix[i][n] == k or matrix[n][j] == k: #같은게 발견된다면
            return False
        n += 1

    #네모 안에서 체크
    x = (i//3)*3
    y = (j//3)*3
    for a in range(x, x+3):
        for b in range(y, y+3):
            if matrix[a][b] == k: #같은게 발견되면
                return False

    return True

sudoku(zeros[0], 0)

