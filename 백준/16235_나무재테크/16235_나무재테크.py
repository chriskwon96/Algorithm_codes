di = [0, -1, -1, -1, 0, +1, +1, +1]
dj = [+1, +1, 0, -1, -1, -1, 0, +1]

N, M, K = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)] #각칸에 추가되는 양분의 양

trees = [[[] for _ in range(N)] for _ in range(N)]
earth = [[5]*N for _ in range(N)]

for _ in range(M):
  x,y,z = map(int, input().split())
  trees[x-1][y-1].append(z)

for _ in range(K):
  #spring
  for i in range(N):
    for j in range(N):
      if trees[i][j]:
        for idx in range(len(trees[i][j])):
          if trees[i][j][idx] <= earth[i][j]:
            earth[i][j] -= trees[i][j][idx]
            trees[i][j][idx] += 1
            if idx == len(trees[i][j])-1:
              idx += 1
          else:
            break

        # print(idx)
        #summer
        for dead_tree in trees[i][j][idx:]:
          earth[i][j] += dead_tree//2
        trees[i][j] = trees[i][j][:idx]

  # for t in trees:
  #   print(t)

  for i in range(N):
    for j in range(N):
      earth[i][j] += A[i][j]
      if trees[i][j]:
        for tree in trees[i][j]:
          if tree % 5 == 0:
            for k in range(8):
              ni, nj = i+di[k], j+dj[k]
              if 0<=ni<N and 0<=nj<N :
                trees[ni][nj].insert(0, 1)

total = 0
for i in range(N):
  for j in range(N):
    if trees[i][j]:
      total += len(trees[i][j])

print(total)







