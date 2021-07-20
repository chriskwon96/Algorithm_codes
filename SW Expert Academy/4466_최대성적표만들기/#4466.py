T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))

    scores.sort()
    total = sum(scores[N-K:])

    print('#{} {}'.format(t, total))