T = int(input())
S = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for t in range(1, T+1):
    N = int(input())
    result = [0]*8

    for i in range(8):
        while S[i] <= N:
            result[i] += 1
            N = N - S[i]

    print("#{}".format(t))
    print(' '.join(list(map(str, result))))