import sys

N, M = map(int, sys.stdin.readline().split())
my_list = list(range(1, N+1))

final_arr = [0]*M

def perm4(cnt, start):
    if cnt == M:
        print(*final_arr)
    else:
        for i in range(start, N):
            final_arr[cnt] = my_list[i]
            perm4(cnt+1, i)

perm4(0,0)

