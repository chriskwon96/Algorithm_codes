N, M = map(int, input().split())
matrix = [list(map(str, input())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'B':
            matrix[i][j] = 0
        else:
            matrix[i][j] = 1
repaint1 = [[0]*(M-7) for _ in range(N-7)]
repaint2 = [[0]*(M-7) for _ in range(N-7)]
for i in range(N-7):
    for j in range(M-7):
        for k in range(i, i+8):
            for l in range(j, j+8):
                if ((k-i + l-j) % 2) and matrix[i][j] == matrix[k][l]:
                    repaint1[i][j] += 1
                if ((k-i + l-j) % 2 == 0) and matrix[i][j] != matrix[k][l]:
                    repaint1[i][j] += 1

for i in range(N-7):
    for j in range(M-7):
        for k in range(i, i+8):
            for l in range(j, j+8):
                if ((k-i + l-j) % 2) and not(matrix[i][j]) == matrix[k][l]:
                    repaint2[i][j] += 1
                if ((k-i + l-j) % 2 == 0) and not(matrix[i][j]) != matrix[k][l]:
                    repaint2[i][j] += 1

minn = 64
for i in range(N-7):
    for j in range(M-7):
        if repaint1[i][j] < minn:
            minn = repaint1[i][j]
        if repaint2[i][j] < minn:
            minn = repaint2[i][j]
print(minn)
