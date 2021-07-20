def bfs(S):
    visited[S] = 1

    queue.append(S)
    while queue:
        node = queue.pop(0)
        step = visited[node]
        for j in range(V):
            if matrix[node][j] == 1 and not visited[j]:
                if j==G-1:
                    return step
                else:
                    visited[j] = step+1
                    queue.append(j)
    return 0


T = int(input())
for t in range(1, T+1):
    V,E = map(int, input().split())
    matrix=[[0]*V for _ in range(V)]
    edges = [list(map(int,input().split())) for _ in range(E)]
    S,G = map(int, input().split())
    for edge in edges:
        x,y=edge[0]-1, edge[1]-1
        matrix[x][y], matrix[y][x] =1,1
    visited=[0]*V
    queue = []
    print('#{} {}'.format(t, bfs(S-1)))
