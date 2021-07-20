N = int(input())
di = [0, +1, +1, +1, 0, -1, -1, -1] # (ud) (lr) (1) (-1)
dj = [+1, +1, 0, -1, -1, -1, 0, +1]
matrix = [[0]*19 for _ in range(19)]

n = 0
while n < N:
    # 바둑돌 놓기
    r, c = map(int, input().split())
    r = r - 1
    c = c - 1
    if n % 2: # N이 홀수
        matrix[r][c] = 2
    else:
        matrix[r][c] = 1
    n += 1
    flag = 0

    V = [0]*8
    for k in range(8):
        ni = r + di[k]
        nj = c + dj[k]

        while (0 <= ni < 19) and (0 <= nj < 19):
            if matrix[ni][nj] == matrix[r][c]:  # 같은 놈 발견하면
                V[k] += 1
                ni += di[k]
                nj += dj[k]
                if (ni < 0 or ni > 18) or (nj < 0 or nj > 18) or matrix[ni][nj] != matrix[r][c]:
                    break
            else:
                break

    for i in range(4):
        if V[i] + V[i+4] == 4:
            flag = 1
            break
    if flag:
        break

if flag:
    print(n)
else:
    print(-1)


