def brute(tries):
    global prize
    if tries < swaps: #횟수가 남았을 때
        for i in range(len(cards)-1):
            for j in range(i+1, len(cards)):
                cards[i], cards[j] = cards[j], cards[i] #swap
                new_num = ''.join(cards)
                if new_num not in data[tries]: # tries번 swap한거 중 중복되는게 없다면
                    data[tries].append(new_num)
                    brute(tries+1)
                cards[i], cards[j] = cards[j], cards[i]
    else:
        if prize < int(''.join(cards)):
            prize = int(''.join(cards))



T = int(input())
for t in range(1, T+1):
    cards, swaps = map(int, input().split())
    cards = list(str(cards))
    data = [[] for _ in range(swaps)] #memo
    prize = 0
    brute(0)
    print('#{} {}'.format(t, prize))


