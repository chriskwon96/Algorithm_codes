import sys
N, M = map(int, sys.stdin.readline().split())
my_list = list(range(1, N+1))

final_arr = [0]*M

def perm3(cnt):
    if cnt == M:
        print(*final_arr)
    else:
        for i in range(N):
            final_arr[cnt] = my_list[i]
            perm3(cnt+1)

perm3(0)


