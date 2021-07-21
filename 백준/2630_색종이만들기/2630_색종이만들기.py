

def paper_cut(start_i, start_j, n): #시작 좌표와 한변의 길이
  global white_paper, blue_paper
  if n == 1:
    if matrix[start_i][start_j] == 0:
      white_paper += 1
    else:
      blue_paper += 1
  else:
    flag = 1 #색종이 모두가 같은 색인지 판단
    crit = matrix[start_i][start_j] #기준점

    for i in range(start_i, start_i+n):
      if flag:
        for j in range(start_j, start_j+n):
          if crit != matrix[i][j]:
            flag = 0
            break
      else:
        break

    if flag == 0: #다른 색이 있다면
      paper_cut(start_i, start_j, n // 2)
      paper_cut(start_i + n // 2, start_j, n // 2)
      paper_cut(start_i, start_j + n // 2, n // 2)
      paper_cut(start_i + n // 2, start_j + n // 2, n // 2)
    else: #모두 같은 색이라면
      if crit == 0:
        white_paper += 1
      else:
        blue_paper += 1


N = int(input())
#N = 10
matrix = [list(map(int, input().split())) for _ in range(N)]
blue_paper, white_paper = 0,0

paper_cut(0,0,N)

print(white_paper)
print(blue_paper)


