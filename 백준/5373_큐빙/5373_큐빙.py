def turnface(face, dir):
  if dir == '+':
    [face[0][0], face[0][1], face[0][2]], [face[0][2], face[1][2], face[2][2]], [face[2][2], face[2][1], face[2][0]], [face[2][0], face[1][0], face[0][0]] = \
    [face[2][0], face[1][0], face[0][0]], [face[0][0], face[0][1], face[0][2]], [face[0][2], face[1][2], face[2][2]], [face[2][2], face[2][1], face[2][0]]
  else:
    [face[2][0], face[1][0], face[0][0]], [face[0][0], face[0][1], face[0][2]], [face[0][2], face[1][2], face[2][2]], [face[2][2], face[2][1], face[2][0]] = \
    [face[0][0], face[0][1], face[0][2]], [face[0][2], face[1][2], face[2][2]], [face[2][2], face[2][1], face[2][0]], [face[2][0], face[1][0], face[0][0]]



tc = int(input()) #테스트케이스의 개수

for t in range(tc):
  N = int(input())
  turns = list(input().split())

  U = [['w']*3 for _ in range(3)]
  D = [['y']*3 for _ in range(3)]
  F = [['r']*3 for _ in range(3)]
  B = [['o']*3 for _ in range(3)]
  L = [['g']*3 for _ in range(3)]
  R = [['b']*3 for _ in range(3)]

  for turn in turns:
    if turn[0] == 'U':
      if turn[1] == '+':
        [B[0]], [R[0]], [F[0]], [L[0]] = [L[0]], [B[0]], [R[0]], [F[0]]
      else:
        [L[0]], [B[0]], [R[0]], [F[0]] = [B[0]], [R[0]], [F[0]], [L[0]]
      turnface(U, turn[1])
    elif turn[0] == 'D':
      if turn[1] == '+':
        [F[2]], [R[2]], [B[2]], [L[2]] = [L[2]], [F[2]], [R[2]], [B[2]]
      else:
        [L[2]], [F[2]], [R[2]], [B[2]] = [F[2]], [R[2]], [B[2]], [L[2]]
      turnface(D, turn[1])
    elif turn[0] == 'F':
      if turn[1] == '+':
        [U[2][0], U[2][1], U[2][2]], [R[0][0], R[1][0], R[2][0]], [D[0][2], D[0][1], D[0][0]], [L[2][2], L[1][2], L[0][2]] = \
        [L[2][2], L[1][2], L[0][2]], [U[2][0], U[2][1], U[2][2]], [R[0][0], R[1][0], R[2][0]], [D[0][2], D[0][1], D[0][0]]
      else:
        [L[2][2], L[1][2], L[0][2]], [U[2][0], U[2][1], U[2][2]], [R[0][0], R[1][0], R[2][0]], [D[0][2], D[0][1], D[0][0]] = \
        [U[2][0], U[2][1], U[2][2]], [R[0][0], R[1][0], R[2][0]], [D[0][2], D[0][1], D[0][0]], [L[2][2], L[1][2], L[0][2]]
      turnface(F, turn[1])
    elif turn[0] == 'B':
      if turn[1] == '+':
        [U[0][2], U[0][1], U[0][0]], [L[0][0], L[1][0], L[2][0]], [D[2][0], D[2][1], D[2][2]], [R[2][2], R[1][2], R[0][2]] = \
        [R[2][2], R[1][2], R[0][2]], [U[0][2], U[0][1], U[0][0]], [L[0][0], L[1][0], L[2][0]], [D[2][0], D[2][1], D[2][2]]
      else:
        [R[2][2], R[1][2], R[0][2]], [U[0][2], U[0][1], U[0][0]], [L[0][0], L[1][0], L[2][0]], [D[2][0], D[2][1], D[2][2]] = \
        [U[0][2], U[0][1], U[0][0]], [L[0][0], L[1][0], L[2][0]], [D[2][0], D[2][1], D[2][2]], [R[2][2], R[1][2], R[0][2]]
      turnface(B, turn[1])
    elif turn[0] == 'L':
      if turn[1] == '+':
        [U[0][0], U[1][0], U[2][0]], [F[0][0], F[1][0], F[2][0]], [D[0][0], D[1][0], D[2][0]], [B[2][2], B[1][2], B[0][2]] = \
        [B[2][2], B[1][2], B[0][2]], [U[0][0], U[1][0], U[2][0]], [F[0][0], F[1][0], F[2][0]], [D[0][0], D[1][0], D[2][0]]
      else:
        [B[2][2], B[1][2], B[0][2]], [U[0][0], U[1][0], U[2][0]], [F[0][0], F[1][0], F[2][0]], [D[0][0], D[1][0], D[2][0]] = \
        [U[0][0], U[1][0], U[2][0]], [F[0][0], F[1][0], F[2][0]], [D[0][0], D[1][0], D[2][0]], [B[2][2], B[1][2], B[0][2]]
      turnface(L, turn[1])
    else:
      if turn[1] == '+':
        [U[2][2], U[1][2], U[0][2]], [B[0][0], B[1][0], B[2][0]], [D[2][2], D[1][2], D[0][2]], [F[2][2], F[1][2], F[0][2]] = \
        [F[2][2], F[1][2], F[0][2]], [U[2][2], U[1][2], U[0][2]], [B[0][0], B[1][0], B[2][0]], [D[2][2], D[1][2], D[0][2]]
      else:
        [F[2][2], F[1][2], F[0][2]], [U[2][2], U[1][2], U[0][2]], [B[0][0], B[1][0], B[2][0]], [D[2][2], D[1][2], D[0][2]] = \
        [U[2][2], U[1][2], U[0][2]], [B[0][0], B[1][0], B[2][0]], [D[2][2], D[1][2], D[0][2]], [F[2][2], F[1][2], F[0][2]]
      turnface(R, turn[1])

  for u in U:
    print("".join(u))




