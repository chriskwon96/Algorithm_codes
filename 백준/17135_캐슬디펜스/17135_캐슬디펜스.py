import itertools
import copy

def kill(archers):
  killed = 0

  mmatrix = copy.deepcopy(matrix)
  while mmatrix != empty:
    final_enemy = set()
    for archer in archers: #각 궁수에 대해서 적 찾기

      enemy = dict()
      for i in range(N):
        for j in range(M):
          if mmatrix[i][j] and abs(i+1)+abs(j-archer) <= D: #죽일 수 있는 적이 존재한다면
            enemy[(i,j)] = abs(i+1)+abs(j-archer)
      if enemy:
        d = min(enemy.values()) #최소거리 찾아
        closest_enemy = [k for k,v in enemy.items() if v==d] #최소거리에 있는 적 찾기
        closest_enemy.sort(key=lambda ele:ele[1])#그중 가장 왼쪽 적 찾기
        # ex,ey = closest_enemy[0] #enemy_x, enemy_y
        final_enemy.add(closest_enemy[0])

    if final_enemy:
      for fe in final_enemy:
        mmatrix[fe[0]][fe[1]] = 0

    killed += len(final_enemy)

    for i in range(1,N): #한칸씩 땡기기
      mmatrix[i-1] = mmatrix[i]
    mmatrix[N-1] = [0]*M


  return killed


N, M, D = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
for i in range(N // 2):  # 위아래 바꾸기
  matrix[i], matrix[N - 1 - i] = matrix[N - 1 - i], matrix[i]
empty = [[0]*M for _ in range(N)]

max_killed = 0

combs = list(itertools.combinations(range(M), 3))

for comb in combs:
  killed = kill(comb)
  if killed > max_killed:
    max_killed = killed

print(max_killed)

