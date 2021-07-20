# 마을의 개수를 return
def bfs(N, K):
    while q:
        node = q.pop(0)
        start, dis = node[0], node[1]
        for k in range(1, N + 1):
            if matrix[start][k] != 0 and dis + matrix[start][k] <= K and v[start][k] == 0:
                v[start][k] = 1
                q.append([k, dis + matrix[start][k]])
                ans.add(k)


def solution(N, road, K):
    global q, matrix, ans, v
    matrix = [[0] * (N + 1) for _ in range(N + 1)]
    for r in road:
        if matrix[r[0]][r[1]] == 0 or matrix[r[0]][r[1]] > r[2]:
            matrix[r[0]][r[1]] = r[2]
            matrix[r[1]][r[0]] = r[2]
    q = [[1, 0]]
    v = [[0] * (N + 1) for _ in range(N + 1)]
    ans = set()
    bfs(N, K)

    return len(ans)

#
N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3

# N = 6
# road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
# K = 4

print(solution(N, road, K))
print(ans)

