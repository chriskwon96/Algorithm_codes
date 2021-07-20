T = int(input())
for t in range(1,T+1):

    N = int(input())

    given = [list(map(int, input().split())) for _ in range(N)]

    new_matrix = []
    tilt = []
    for _ in range(3):
        new_matrix = []

        for i in range(N):
            row = []

            for j in range(N-1, -1, -1):
                row.append(given[j][i])
            new_matrix.append(row)
            tilt.append(''.join(list(map(str, row))))
        given = new_matrix


    print('#{}'.format(t))
    for j in range(N):

        for i in range(0, 3*N, N):

            print(tilt[i+j], end = ' ')
        print()

