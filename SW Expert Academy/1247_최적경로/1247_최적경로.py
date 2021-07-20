def routes(n, dis):
    global min_dis

    if n == N:
        new_dis = dis + (abs(p[N-1][0]-home[0])+abs(p[N-1][1]-home[1]))
        if new_dis < min_dis:
            min_dis = new_dis
    else:
        for i in range(N):
            if v[i] == 0:
                v[i] = 1
                p[n] = houses[i]
                if n == 0:
                    new_dis = dis + (abs(company[0]-houses[i][0])+abs(company[1]-houses[i][1]))
                else:
                    new_dis = dis + (abs(p[n - 1][0] - p[n][0]) + abs(p[n - 1][1] - p[n][1]))
                if new_dis < min_dis:
                    routes(n+1, new_dis)
                v[i] = 0



T = int(input())
for t in range(1, T+1):
    N = int(input())
    given = list(map(int, input().split()))
    company = (given[0], given[1])
    home = (given[2], given[3])
    houses = []
    for i in range(2, N+2):
        houses.append((given[2*i], given[2*i+1]))

    v = [0]*N #visited
    p = [0]*N
    min_dis = 1000000000

    routes(0, 0)
    print('#{} {}'.format(t, min_dis))





