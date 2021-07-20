
T= int(input())
for t in range(1,T+1):
    inputs = list(map(int, input().split()))
    L, U, X = inputs[0], inputs[1], inputs[2]
    result = 0
    if X < L:  # 운동이 부족하다면
        result = L - X
    elif L < X < U:  # 적절하다면
        result = 0
    else:
        result = -1

    print('#{} {}'.format(t,result))

