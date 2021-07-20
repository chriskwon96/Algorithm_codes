di = [0, +1]
dj = [+1, 0]

def backtracking(x,y,my_sum):
    global min_sum
    if x==N-1 and y==N-1: #마지막에 도달
        if my_sum < min_sum:
            min_sum = my_sum
    else:
        if my_sum > min_sum:
            return
        for k in range(2):
            xx,yy = x+di[k], y+dj[k]
            if xx<N and yy<N: #범위안에 있다면
                backtracking(xx, yy, my_sum+matrix[xx][yy])

T = int(input())
for t in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    my_sum = matrix[0][0]
    min_sum = 100000000
    backtracking(0,0,my_sum)
    print('#{} {}'.format(t, min_sum))
