T = int(input())
for t in range(1, T+1):
    N, limit = map(int, input().split())
    taste = [0]*N
    cals = [0]*N
    scores = []
    for i in range(N):
        taste[i], cals[i] = map(int, input().split())

    for i in range(1 << N):
        cal_idx = []
        for j in range(N):
            if i & (1<<j):
                cal_idx.append(j)
        cal_sum = 0
        score = 0
        for k in cal_idx:
            cal_sum += cals[k]
        if cal_sum <= limit:
            for k in cal_idx:
                score += taste[k]
            scores. append(score)

    print('#{} {}'.format(t, max(scores)))
