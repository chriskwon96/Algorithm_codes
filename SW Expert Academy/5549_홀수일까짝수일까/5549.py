    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        if N % 2:
            result = 'Odd'
        else:
            result = 'Even'
        print('#{} {}'.format(t, result))
