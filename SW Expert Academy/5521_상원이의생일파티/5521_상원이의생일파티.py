
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        i, j = map(int, input().split())
        matrix[i][j], matrix[j][i] = 1, 1
    friends = [1]
    ans = {1}
    for k in range(N+1):
        if matrix[1][k]:
            friends.append(k)
            ans.add(k)
    for friend in friends:
        for k in range(N+1):
            if matrix[friend][k]:
                ans.add(k)
    print('#{} {}'.format(t, len(ans)-1))