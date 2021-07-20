R, C, M = map(int, input().split())
matrix = [[0] * C for _ in range(R)]
for _ in range(M):
  r, c, s, d, z = map(int, input().split())
  matrix[r-1][c-1] = [s,d,z]

for m in matrix:
  print(m)