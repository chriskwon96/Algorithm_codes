import sys
N = int(sys.stdin.readline())

def nq(row, col):
    global cnt

    if row == N-1:
        cnt += 1
        return
    else: #다음줄 검사
        for m in range(N): #다음줄의 모든 col
            i = 0
            while i < len(stack): # i번째 퀸
                if (m != stack[i][1]) and ((stack[i][0] - stack[i][1]) != (row+1 - m)) and (sum(stack[i]) != row+1+m):
                    i += 1
                    if i == len(stack): #모든 퀸에 대한 검사를 마쳤다면
                        stack.append([row+1, m])
                        nq(row+1, m)
                        stack.pop()
                else:
                    break


cnt = 0
for j in range(N):
    stack = [[0,j]]
    nq(0, j)

print(cnt)
