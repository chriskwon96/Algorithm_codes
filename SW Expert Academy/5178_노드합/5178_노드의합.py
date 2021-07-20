T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    nodes = [0]*(N+1)
    for _ in range(M):
        i, j = map(int, input().split())
        nodes[i]=j
    for i in range(N, 0, -1):
        if nodes[i] == 0:
            if 2*i+1 <= N:
                nodes[i] = nodes[2*i]+nodes[2*i+1]
            else:
                nodes[i] = nodes[2*i]
            if i == L:
                break
    print("#{} {}".format(t, nodes[L]))
