


N, L = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

# row
for i in range(N):
    flag = 0
    slope = [0]*N
    for j in range(N-1):
        if flag: break
        sub = matrix[i][j+1]-matrix[i][j]
        if abs(sub) > 1:
            flag = 2
            break
        else:
            if sub == 1:
                for k in range(j + 1 - L, j + 1):
                    if 0 <= k < N and not slope[k]:
                        slope[k] = sub
                    else: #경사로가 범위를 벗어나거나 경사로가 이미 놓여있는 경우
                        flag = 1
                        break

            elif sub == -1:
                for k in range(j+1, j+L+1):
                    if 0<=k<N and not slope[k]:
                        slope[k] = sub
                    else:
                        flag = 1
                        break
    if flag == 0 :
        cnt += 1

for j in range(N):
    flag = 0
    slope = [0]*N
    for i in range(N-1):
        if flag: break
        sub = matrix[i+1][j]-matrix[i][j]
        if abs(sub) > 1:
            flag=2
            break
        else:
            if sub == 1:
                for k in range(i+1-L, i+1):
                    if 0<=k<N and not slope[k]:
                        slope[k] = sub
                    else:
                        flag = 1
                        break
            elif sub == -1:
                for k in range(i+1, i+L+1):
                    if 0<=k<N and not slope[k]:
                        slope[k] = sub
                    else:
                        flag = 1
                        break
    if flag == 0:
        cnt += 1


print(cnt)



