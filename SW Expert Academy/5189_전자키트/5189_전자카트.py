def back(S, my_sum, cnt):
    global final_sum
    if cnt == N:
        if final_sum > my_sum+matrix[S][0]:
            final_sum = my_sum+matrix[S][0]
    else:
        if final_sum < my_sum:
            return
        for k in range(N):
            if check[k] == 0:
                check[k] = 1
                back(k, my_sum+matrix[S][k], cnt+1)
                check[k]=0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    check = [1]+[0]*(N-1)
    final_sum=100000000
    back(0,0,1)
    print('#{} {}'.format(t, final_sum))





