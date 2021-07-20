N = int(input())
di = [0, +1, +1, +1, 0, -1, -1, -1]
dj = [+1, +1, 0, -1, -1, -1, 0, +1]
matrix = [[0]*19 for _ in range(19)]

n = 0
while n < N:
    # 바둑돌 놓기
    r, c = map(int, input().split())
    r = r - 1
    c = c - 1
    if n % 2: # N이 홀수
        matrix[r][c] = 1
    else:
        matrix[r][c] = 2
    n += 1
    flag = 0

    #판 중에서 돌이 있는 놈만 확인
    for i in range(19):
        for j in range(19):
            if matrix[i][j] != 0:

                #주변 확인
                for k in range(8):
                    ni = i+di[k]
                    nj = j+dj[k]
                    cnt = 1
                    while (0 <= ni < 19) and (0 <= nj < 19):
                        if matrix[ni][nj] == matrix[i][j]: #같은 놈 발견하면
                            cnt += 1
                            ni += di[k]
                            nj += dj[k]
                            if cnt == 5:
                                if (ni < 0 or ni > 18) or (nj < 0 or nj > 18) or matrix[ni][nj] != matrix[i][j]:
                                    flag = 1
                                    break
                        else: #같은놈이 아니라면
                            break
                    if flag:
                        break
            if flag:
                break
        if flag:
            break
    if flag:
        break

if (n == N) and flag == 0:
    print(-1)
else:
    print(n)


