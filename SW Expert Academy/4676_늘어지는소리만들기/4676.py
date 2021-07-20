T = int(input())

for t in range(1, T+1):
    word = list(input())
    H = int(input())
    location = list(map(int, input().split()))

    for i in range(len(word)+1):
        j = 2*i
        word.insert(j, '')

    for h in location:
        word[2*h] += '-'

    print('#{} {}'.format(t, ''.join(word)))