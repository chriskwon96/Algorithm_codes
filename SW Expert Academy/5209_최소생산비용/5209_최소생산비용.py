def back(i, my_sum):
    global min_sum
    if my_sum <= min_sum:
        if i == N:
            min_sum = my_sum
        else:
            for j in range(N):
                if check[j] == 0:
                    check[j] = 1
                    back(i+1, my_sum + matrix[i][j])
                    check[j] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    check = [0]*N
    min_sum = 100000000
    back(0,0)
    print('#{} {}'.format(t, min_sum))
