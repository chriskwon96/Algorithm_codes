N = int(input())
coors = []
for n in range(N):
    x,y = map(int, input().split())
    coors.append([x, y])

# for j in range(2):
#     for i in range(N):
#         for k in range(i):
#             if coors[k][j] > coors[k+1][j]:
#                 coors[k][j], coors[k+1][j] = coors[k+1][j], coors[k][j]
#
coors.sort()

for coor in coors:
    for i in coor:
        print(i, end=' ')
    print()
