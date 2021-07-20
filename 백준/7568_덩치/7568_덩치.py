N = int(input())
people = []
for _ in range(N):
    x, y = map(int, input().split())
    people.append([x,y])

rank = [1]*N
for i in range(N):
    for j in range(N):
        if i != j:
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                rank[i] += 1
print(' '.join(map(str, rank)))



