#bfs
# global uni
di = [0, -1, 0, +1]
dj = [+1, 0, -1, 0]

def bfs(start):
  q = [start]
  uni = [start]
  while q:
    [x,y] = q.pop(0)
    for k in range(4):
      ni, nj = x+di[k], y+dj[k]
      if 0<=ni<N and 0<=nj<N:
        # print(abs(A[x][y]-A[ni][nj]))
        if L <= abs(A[x][y]-A[ni][nj]) <=R and not checked[ni][nj]:
          q.append([ni,nj])
          uni.append([ni,nj])
          checked[ni][nj] = 1
  # print(uni)
  unis.append(uni)




N, L, R = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]

q = []
cnt = 0

while True:
  flag = 0
  checked = [[0] * N for _ in range(N)]
  unis = []
  for i in range(N):
    for j in range(N):
      for k in range(4):
        ni, nj = i+di[k], j+dj[k]
        if 0<=ni<N and 0<=nj<N:
          if L <= abs(A[i][j]-A[ni][nj]) <= R and not checked[ni][nj]:
            flag = 1
            checked[i][j] = 1
            bfs([i,j])
  if flag:
    cnt += 1

    for u in unis:
      s = 0
      for coor in u:
        s += A[coor[0]][coor[1]]
      avg = s // len(u)
      for coor in u:
        A[coor[0]][coor[1]] = avg

  else:
    break

print(cnt)



