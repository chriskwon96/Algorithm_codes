T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    # N: number of horns M: num of animals

    bi = N - M
    uni = M - bi

    print("#{} {} {}".format(t, uni, bi))