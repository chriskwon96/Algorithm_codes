



def dfs(i, n, computers, checked):
  q = [computers[i]]
  while q:
    here = q.pop(0)
    for j in range(n):
      if here[j] == 1 and checked[j] == 0:
        q.append(computers[j])
        checked[j] = 1




def solution(n, computers):
  checked = [0]*n
  cnt = 0
  for i in range(n):
    if checked[i] == 0 :
      dfs(i, n, computers, checked)
      cnt += 1
  return cnt

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))