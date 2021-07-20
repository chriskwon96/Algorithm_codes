T = int(input())

for t in range(1, T+1):
    scores = list(map(int, input().split()))
    for idx in range(len(scores)):
        if scores[idx] < 40:
            scores[idx]=40

    avg = sum(scores)//len(scores)
    print('#{} {}'.format(t, avg))