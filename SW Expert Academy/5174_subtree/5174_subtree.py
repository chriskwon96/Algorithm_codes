def bfs(N):
    global cnt
    while queue:
        node = queue.pop(0)
        for i in range(E+1):
            if matrix[node][i] == 1:
                queue.append(i)
                cnt += 1



T = int(input())
for t in range(1, T+1):
    E, N = map(int, input().split())
    nums = list(map(int, input().split()))
    matrix = [[0]*(E+1) for _ in range(E+1)]
    for i in range(0, len(nums), 2):
        matrix[nums[i]-1][nums[i+1]-1] = 1
    queue = [N-1]
    cnt = 1
    bfs(N)
    print("#{} {}".format(t, cnt))

