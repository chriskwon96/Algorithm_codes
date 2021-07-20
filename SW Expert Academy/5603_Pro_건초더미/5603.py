T = int(input())

for t in range(1, T+1):
    N = int(input())
    hays = []
    for _ in range(N):
        hays.append(int(input()))

    avg = sum(hays) // N
    diff = 0
    for i in range(N):
        if hays[i] > avg:
            diff += hays[i] - avg
    print('#{} {}'.format(t, diff))

