def perm(n, N):
    if n == N:
        print(p)
    else:
        for i in range(N):
            if used[i] == 0:
                used[i] = 1
                p[n] = my_list[i]
                perm(n + 1, N)
                used[i] = 0


N = int(input())
my_list = list(input().split())
used = [0]*N
p = [0]*N

perm(0,N)





