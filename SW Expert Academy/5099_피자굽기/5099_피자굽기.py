T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    cheeses = list(map(int, input().split()))
    out = []
    for i,ch in enumerate(cheeses):
        cheeses[i] = [i,ch]
    oven = cheeses[:N]
    cheeses = cheeses[N:]
    while len(out) < M:
        for i in range(N):
            if oven[i][1] //2 == 0 and (oven[i][0] not in out):
                if cheeses:
                    out.append(oven.pop(i)[0])
                    oven.insert(i,cheeses.pop(0))
                else:
                    out.append(oven[i][0])
            else:
                oven[i][1] = oven[i][1]//2
    print('#{} {}'.format(t, out[-1]+1))