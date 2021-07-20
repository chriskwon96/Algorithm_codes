T = int(input())

for t in range(1, T+1):
    N = int(input())
    n = 0
    given = []
    while n < N :
        giv = list(map(int, input().split()))
        given.extend(giv)
        n += len(giv)

    nums = []
    flag = 1
    for k in range(N):
        checks = list(range(10**k, 10**(k+1)))
        checks.insert(0,0)
        for i in range(N-k):
            A = ''
            for j in range(i, i+k+1):
                A += str(given[j])
            nums.append(int(A))

        for check in checks:
            if check not in nums:
                result = check
                flag = 0
                break
        if flag == 0 :
            break

    print('#{} {}'.format(t, result))
