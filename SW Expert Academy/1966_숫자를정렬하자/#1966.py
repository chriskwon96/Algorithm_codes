
T = int(input())

for t in range(1, T+1):
    N = int(input())
    given = list(map(int, input().split()))

    #bubble sort

    for i in range(N-1):
        for j in range(N-i-1):
            if given[j] > given[j+1]:
                given[j], given[j+1] = given[j+1], given[j]

    given = ' '.join(list(map(str, given)))

    print('#{} {}'.format(t,given))
