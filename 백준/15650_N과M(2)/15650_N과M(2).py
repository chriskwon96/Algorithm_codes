import sys

N, M = map(int, sys.stdin.readline().split())
my_list = list(range(1, N+1))
check = [0]*N
final_arr = [0]*M

def perm(cnt, start):
    if cnt == M:
        print(*final_arr)
    else:
        for i in range(start, N):
            if check[i] == 0:
                check[i] = 1
                final_arr[cnt] = my_list[i]
                perm(cnt+1, i)
                check[i] = 0

perm(0,0)



