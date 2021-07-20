T = int(input())

di = [0, -1, 0, +1, 0]
dj = [1, 0, -1, 0, +1]

for t in range(1, T+1):
    print('#{}'.format(t))
    N = int(input())
    cnt = 1
    matrix = [[0]*N for _ in range(N)]

    # matrix 'end'로 둘러싸기
    for row in matrix:
        row.append('end')
        row.insert(0, 'end')
    matrix = matrix + [['end']*(N+2)]

    i = j = k = 0

    ni = i
    nj = j
    while cnt <= N*N:

        if matrix[ni+di[k]][nj+dj[k]] == 0: #다음칸이 0이라면
            ni = ni+di[k] # 다음칸으로 옮겨주고
            nj = nj+dj[k]
            matrix[ni][nj] = cnt #해당칸에 값 넣기
            cnt += 1

        else: # 다음칸이 'end'거나 이미 차있다면
            k += 1
            k = k % 4

    matrix.pop()
    for row in matrix:
        row = [x for x in row if x != 'end']

        print(' '.join(list(map(str, row))))
