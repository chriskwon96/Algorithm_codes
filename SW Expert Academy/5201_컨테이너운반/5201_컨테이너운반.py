T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    wi = sorted(list(map(int, input().split())), reverse=True)
    ti = sorted(list(map(int, input().split())), reverse=True)
    total = 0
    for i in range(len(ti)):
        truck = ti[i]
        for j in range(len(wi)):
            w = wi[j]
            if w<=truck:
                total += w
                wi.pop(j)
                break
    print('#{} {}'.format(t, total))










