di = [0, 0, +1, -1]
dj = [-1, +1, 0, 0]

def dfs(coor, n):
    visited.append(coor) # 현재좌표 저장
    matrix[coor[0]][coor[1]] = n # 구역의 번호 저장
    for k in range(4): #주변을 검사
        ni = coor[0] + di[k]
        nj = coor[1] + dj[k]
        if (0 <= ni < T) and (0 <= nj < T) and (matrix[ni][nj] == 1) and ([ni, nj] not in visited): # 방문하지 않은 곳이라면
            dfs([ni, nj], n)


T = int(input())
matrix = [list(map(int, input())) for _ in range(T)]
visited = []
result = {}
i = 0
j = 0
n = 1
while i < T:
    while j < T:
            if (matrix[i][j] == 1) and ([i, j] not in visited):
                dfs([i, j], n)
                n += 1
                i = 0
                j = 0
            else:
                j += 1
    i += 1
    j = 0

for row in matrix:
    for i in row:
        if i != 0:
            if i not in result:
                result[i] = 1
            else:
                result[i] += 1

print(max(result))
houses = []
for val in result.values():
    houses.append(val)

houses.sort()
for house in houses:
    print(house)

