T = int(input())
for t in range(1, T+1):

    N = int(input()) #노선의 개수
    A = []
    for i in range(1, N+1):
        a = tuple(map(int, input().split()))
        A.append(a)

    P = int(input())
    C = []
    for j in range(1, P+1):
        C.append(int(input()))
    total = [0]*len(C)

    for a in A:
        for aa in range(a[0], a[1]+1):
            for k in range(len(total)):
                if aa == C[k]:
                    total[k] += 1

    print('#{}'.format(t), end=' ')
    for i in total:
        print(i, end = ' ')
    print()
