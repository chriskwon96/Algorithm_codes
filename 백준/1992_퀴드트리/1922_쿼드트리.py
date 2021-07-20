def func(submatrix, n):

  for i in range(n):
    for j in range(n):
      if submatrix[i][j] != submatrix[0][0]: #다른게 발견된다면
        a = [[submatrix[x][y] for y in range(n//2)] for x in range(n//2)]
        b = [[submatrix[x][y] for y in range(n // 2,n)] for x in range(n//2)]
        c = [[submatrix[x][y] for y in range(n // 2)] for x in range(n // 2, n)]
        d = [[submatrix[x][y] for y in range(n // 2,n)] for x in range(n // 2,n)]
        return '('+func(a, n//2)+func(b, n//2)+func(c, n//2)+func(d, n//2)+')'

  return str(submatrix[0][0])

N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]

ans = func(matrix, N)

print(ans)



