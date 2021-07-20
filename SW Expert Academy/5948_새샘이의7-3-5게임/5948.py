T = int(input())
for t in range(1, T+1):
    num = list(map(int, input().split()))
    A = []
    for i in range(7):
        for j in range(i+1,7):
            for k in range(j+1, 7):
                B = num[i]+num[j]+num[k]
                if B not in A:
                    A.append(B)
    A.sort(reverse=True)
    print('#{} {}'.format(t, A.pop(4)))
