import copy
global blind

di = [0, +1, 0, -1]
dj = [+1, 0, -1, 0]


def watch(i, j, ks, mymatrix):
    for k in ks:
        ni, nj = i + di[k], j + dj[k]
        while 0 <= ni < N and 0 <= nj < M:
            if mymatrix[ni][nj] == 6:
                break
            elif mymatrix[ni][nj] == 0:
                mymatrix[ni][nj] = '#'
            ni += di[k]
            nj += dj[k]
    return mymatrix


def f(n, cctv, matrix):
    global blind
    if not cctv:
        cnt = 0
        for x in range(N):
            for y in range(M):
                if matrix[x][y] == 0:
                    cnt += 1
        if cnt < blind:
            blind = cnt

    else:
        i, j, v = cctv.pop(0)

        if v == 1:
            for k in range(4):
                mymatrix = copy.deepcopy(matrix)
                q = copy.deepcopy(cctv)
                f(n+1, q, watch(i, j, [k], mymatrix))

        elif v == 2:
            mymatrix = copy.deepcopy(matrix)
            q = copy.deepcopy(cctv)
            f(n+1, q, watch(i,j, [0,2], mymatrix))
            mymatrix = copy.deepcopy(matrix)
            q = copy.deepcopy(cctv)
            f(n+1, q, watch(i,j, [1,3], mymatrix))
        elif v == 3:
            for k in range(4):
                mymatrix = copy.deepcopy(matrix)
                q = copy.deepcopy(cctv)
                f(n+1, q, watch(i, j, [k, (k+1)%4], mymatrix))
        elif v == 4:
            for k in range(4):
                mymatrix = copy.deepcopy(matrix)
                q = copy.deepcopy(cctv)
                f(n+1, q, watch(i, j, [k-1, k, (k+1)%4], mymatrix))
        else:
            mymatrix = copy.deepcopy(matrix)
            q = copy.deepcopy(cctv)
            f(n+1, q, watch(i, j, [0,1,2,3], mymatrix))



N, M = map(int, input().split())
matrix = [list(input().split()) for _ in range(N)]
cctv = []
blind = 65

for i in range(N):
    for j in range(M):
        if matrix[i][j].isdigit():
            matrix[i][j] = int(matrix[i][j])
            if 0 < int(matrix[i][j]) < 6:
                cctv.append((i, j, matrix[i][j]))

f(0, cctv, matrix)
print(blind)
# print(matrix)


