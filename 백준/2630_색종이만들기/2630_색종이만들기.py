def put_paper(i,j,size,checked):
  for x in range(size):
    for y in range(size):
      if 0<=i+x<10 and 0<=j+y<10:
        if matrix[i+x][j+y] == 0 or checked[i+x][j+y] == 1:
          return False
      else:
        return False

  return True



def f(cnt, used_paper, checked):
  global min_paper
  if cnt <= min_paper: # 최소 종이보다 지금이 더 적을 경우에만
    for i in range(10): # 모든 칸 중에
      for j in range(10):
        if matrix[i][j] == 1 and checked[i][j] == 0: #종이를 놓을 수 있는데 아직 놓지 않았다면
          # print(i,j)
          # 1-5까지 종이 놓아보기
          for size in range(1, 6):
            if put_paper(i, j, size, checked) is True :
              if used_paper[size] < 5: # 종이를 놓을 수 있다면
                # 종이를 놓았다고 check 하기
                # print(i,j)
                used_paper[size] += 1
                # print(i,j,used_paper,checked)
                for u in range(size):
                  for v in range(size):
                    checked[i+u][j+v] = 1
                f(cnt+1, used_paper, checked)
                used_paper[size] -= 1
                for u in range(size): #check 되돌리기
                  for v in range(size):
                    checked[i+u][j+v] = 0
            else:
              return

    # 모든 칸 다 돌았으면
    if cnt < min_paper:
      min_paper = cnt
  else:
    return



# N = int(input())
N = 10
matrix = [list(map(int, input().split())) for _ in range(10)]
checked = [[0]*N for _ in range(N)]
cnt = 0
min_paper = 1000
used_paper = {1:0, 2:0, 3:0, 4:0, 5:0}

f(cnt, used_paper, checked)

if min_paper == 1000:
  print(-1)
else:
  print(min_paper)
# print(min_paper)

