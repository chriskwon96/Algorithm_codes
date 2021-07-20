
di = [0, 0, +1, -1] #L R D U
dj = [-1, +1, 0, 0]

def dfs(coor, n):
    stack.append(coor)
    visited.append(coor)
    matrix[coor[0]][coor[1]] = n #구역 번호 저장
    while stack: #stack이 비어있지 않다면
        ii, jj = stack.pop()
        for k in range(4):
            ni = ii + di[k]
            nj = jj + dj[k]
            if (0 <= ni < N) and (0 <= nj < M) and (matrix[ni][nj] == 1) and ([ni, nj] not in visited):
                stack.append([ni,nj])
                visited.append([ni, nj])
                matrix[ni][nj] = n

T = int(input())
for t in range(1, T+1):
    # matrix 만들기
    M, N, K = map(int, input().split())
    matrix = [[0]*M for _ in range(N)]
    for _ in range(K):
        s, e = map(int, input().split())
        matrix[e][s] = 1

    stack = []
    maxes = []
    visited = []
    i = 0
    j = 0
    n = 1
    while i < N:
        while j < M:
            if (matrix[i][j] == 1) and ([i, j] not in visited): #초기값
                dfs([i, j], n)
                n += 1
                i = 0
                j = 0
            else:
                j += 1
        i += 1
        j = 0

    for row in matrix:
        maxes.append(max(row))
    print(max(maxes))