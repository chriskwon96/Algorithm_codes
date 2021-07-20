from itertools import combinations

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
chickens = []
houses = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            houses.append([i,j])
        elif matrix[i][j] == 2:
            chickens.append([i,j])

#2=>치킨
combs = list(combinations(chickens, M))
# print(combs)

min_dist = 10000000000
for comb in combs: #모든 가능한 치킨집 조합에 대해
    final_dist = 0
    for house in houses:  #모든 집에 대해
        dist = 1000
        for chicken in comb: #모든 치킨집에 대해

            cur_dist = abs(chicken[0]-house[0])+abs(chicken[1]-house[1])
            # print(house, chicken, cur_dist)
            if cur_dist < dist:
                dist = cur_dist
        # print(house, dist)
        final_dist += dist
        if final_dist >= min_dist:
            break
    if final_dist < min_dist:
        min_dist = final_dist
print(min_dist)



