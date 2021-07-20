T = int(input())
alien = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
for t in range(1, T+1):
    C = [0] * 10
    tc, N = input().split()
    N = int(N)
    given = list(input().split())
    B = [0] * N
    for i in range(N):
        C[alien.index(given[i])] += 1

    for i in range(1, 10):
        C[i] = C[i]+C[i-1]

    for i in range(N-1, -1, -1):
        C[alien.index(given[i])] -= 1
        B[C[alien.index(given[i])]] = given[i]

    print("{}".format(tc))
    print(' '.join(B))
