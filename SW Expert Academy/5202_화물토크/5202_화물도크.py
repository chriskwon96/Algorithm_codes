T = int(input())
for t in range(1, T+1):
    N = int(input())
    schd = []
    for _ in range(N):
        s,e = map(int, input().split())
        schd.append((s,e))
    schd.sort(key=lambda end:end[1])
    schd.sort(key=lambda start:start[0])
    total = 1
    i=-1
    start = schd[-1]
    while i >= -N :
        if schd[i][1]<=start[0]:
            total += 1
            start = schd[i]
        i -= 1
    print('#{} {}'.format(t, total))




