N, M = map(int, input().split())
cards = list(map(int, input().split()))

flag = 0
closest = 1000000000

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            s = cards[i]+cards[j]+cards[k]
            if s == M:
                result = M
                flag = 1
                break
            else:
                if (M > s) and (closest > M-s):
                    closest = M-s
        if flag:
            break
    if flag:
        break

if not flag:
    result = M-closest

print(result)
