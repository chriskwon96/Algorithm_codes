def check(i):
    for j in range(N):
        if matrix[i][j] == 1 and v[j] == 0:
            v[j] = 1
            check(j)


tc = int(input())
for t in range(tc):
    N, M = map(int, input().split())
    given_list = list(map(int, input().split()))
    matrix = [[0]*N for _ in range(N)]
    v = [0]*N
    groups = 0
    for i in range(M):
        matrix[given_list[2*i]-1][given_list[2*i+1]-1], matrix[given_list[2*i+1]-1][given_list[2*i]-1] = 1, 1
    for i in range(N):
        if v[i] == 0:
            groups += 1
            v[i] = 1
            check(i)


    print("#{} {}".format(t+1,groups))






