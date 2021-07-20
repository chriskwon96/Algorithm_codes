di = [-1, +1, 0, 0]
dj = [0, 0, +1, -1]

def move(x,y,d,s):

  if d == 1: #up
    if s >= 2*R:
      s %= 2*R
    if x-s <=0:
      d = 2
    nx,ny = abs(x-s), y

  elif d == 2: #down
    if s >= 2*R:
      s %= 2*R
    if x + s >= R-1:
      d = 1
      nx,ny = R-1-(x+s-R+1), y
    else:
      nx,ny = x+s, y

  elif d==3: #right
    if s >= 2*C:
      s %= 2*C
    if y+s >= C-1:
      d = 4
      nx, ny = x, C-1-(y+s-C+1)
    else:
      nx,ny = x, y+s
  else: #left
    if s >= 2*C:
      s %= 2*C
    if y-s <=0:
      d = 3
    nx,ny = x, abs(y-s)
  return nx, ny, d



R, C, M = map(int, input().split())
matrix = [[0] * C for _ in range(R)]
for _ in range(M):
  r, c, s, d, z = map(int, input().split())
  matrix[r-1][c-1] = [s,d,z]

cnt = 0

j = 0
while j < C:
  # 상어 낚시하기
  for i in range(R):
    if matrix[i][j]:
      cnt += matrix[i][j][2]
      # print(i,j, matrix[i][j][2])
      matrix[i][j] = 0
      break
  #상어 움직이기
  new_matrix = [[0]*C for _ in range(R)]
  for x in range(R):
    for y in range(C):
      if matrix[x][y] :
        [s,d,z] = matrix[x][y]
        nx,ny,nd = move(x,y,d,s)
        print(nx,ny,z)
        if new_matrix[nx][ny]:
          if new_matrix[nx][ny][2] < z:
            new_matrix[nx][ny] = [s,nd,z]
        else:
          new_matrix[nx][ny] = [s,nd,z]
  matrix = new_matrix
  for m in new_matrix: print(m)
  print('====================')
  # 사람이동
  j += 1

print(cnt)


