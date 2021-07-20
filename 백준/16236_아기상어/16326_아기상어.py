di = [-1, 0, 0, +1]
dj = [0, -1, +1, 0]


def bfs(i,j,h):
  global eaten, baby_age
  # print(i,j,h,baby_age)
  checked = [[0] * N for _ in range(N)]
  q = [[i,j,h]]
  checked[i][j] = 1
  cand = []
  while q:
    [x,y,t] = q.pop(0)
    for k in range(4):
      nx, ny = x + di[k], y + dj[k]
      if 0<=nx<N and 0<=ny<N and not checked[nx][ny]:
        if 0 < matrix[nx][ny] < baby_age: #물고기를 먹어야된다면
          cand.append([nx,ny,t+1])
          break

        elif matrix[nx][ny] == baby_age or matrix[nx][ny] == 0: #이동만
          q.append([nx,ny,t+1])
          checked[nx][ny] = 1

  if cand:
    cand.sort(key=lambda ele: (ele[2],ele[0],ele[1]))
    # print(cand)
    # cand.sort(key=lambda ele: ele[0])
    [xx,yy, t] = cand.pop(0)
    matrix[xx][yy] = 0
    eaten += 1
    if eaten == baby_age:
      baby_age += 1
      eaten = 0
    bfs(xx,yy,t)

  print(h)
  exit(0)



N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
checked = [[0]*N for _ in range(N)]

baby_age = 2
eaten = 0


for i in range(N):
  for j in range(N):
    if matrix[i][j] == 9:
      matrix[i][j] = 0
      bfs(i,j,0)

# print(ans)



