di = [0, -1, 0, +1]
dj = [+1, 0, -1, 0]

N = int(input())
matrix = [[0]*N for _ in range(N)]
K = int(input())
for _ in range(K): #사과위치 1로 지정
    i, j = map(int, input().split())
    matrix[i-1][j-1] = 1
L = int(input())
q = [(0,0)] #뱀 몸
X1, k, cnt = 0, 0, 0
flag = 1

for _ in range(L):
    X, C = input().split()
    for _ in range(int(X)-X1):
        head = q[0]
        cnt += 1
        n_x, n_y = head[0]+di[k], head[1]+dj[k]
        if 0<=n_x<N and 0<=n_y<N and ((n_x, n_y) not in q): #다음칸이 판 안에 있고 내 몸이 아니라면
            q.insert(0, (n_x, n_y)) #머리좌표 q에 삽입
            if matrix[n_x][n_y]: #사과라면
                matrix[n_x][n_y] = 0 #사과 지워주기
            else:
                q.pop() #사과가 아니면 꼬리 줄여주기
        else: # 게임이 끝나면
            print(cnt)
            flag = 0
            break
    if not flag:
        break
    X1 = int(X)
    if C == 'L':
        k = (k+1)%4
    else:
        k = (k-1)%4

if flag: #인풋을 다 받아도 끝나지 않았다면
    head = q[0]
    n_x, n_y = head[0]+di[k], head[1]+dj[k]
    while 0<=n_x<N and 0<=n_y<N and ((n_x, n_y) not in q):
        cnt += 1
        q.insert(0, (n_x, n_y))
        if matrix[n_x][n_y]: #사과라면
            matrix[n_x][n_y] = 0 #사과 지워주기
        else:
            q.pop() #사과가 아니면 꼬리 줄여주기
        n_x, n_y = n_x + di[k], n_y + dj[k]

    print(cnt+1)


