T= int(input())

for t in range(1, T+1):

    my_sudoku = [list(map(int, input().split())) for _ in range(9)]

    check = set(range(1,10))
    result = 1
    for i in range(9):
        rol = []
        if set(my_sudoku[i]) != check:
            result = 0
        for j in range(9):
            rol.append(my_sudoku[j][i])
        if set(rol) != check:
            result = 0

    for i in range(0,9,3):
        for j in range(0,9,3):
            sq=[]
            for k in range(i,i+3):
                for l in range(j,j+3):
                    sq.append(my_sudoku[k][l])
            if set(sq) != check:
                result = 0
    print('#{} {}'.format(t,result))

