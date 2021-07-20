T = int(input())
for t in range(1, T+1):
    N = int(input())
    deck = list(input().split())
    result = []
    if N%2:
        for i in range(N//2):
            result.append(deck[i])
            result.append(deck[i+N//2+1])
        result.append(deck[N//2])

    else:
        for i in range(N//2):
            result.append(deck[i])
            result.append(deck[i+N//2])

    print('#{} {}'.format(t, ' '.join(result)))