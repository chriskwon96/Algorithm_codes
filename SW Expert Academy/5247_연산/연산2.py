from _collections import deque

def bfs(x):
    q.append(x)
    while q:
        num, tries = q.popleft()
        if num == M:
            return tries
        else:
            comps=[num+1, num-1, num*2, num-10]
            for new_num in comps:
                if new_num<=1000000 and v[new_num] ==0:
                    q.append((new_num, tries+1))
                    v[new_num] = 1



tc = int(input())
for t in range(tc):
    N, M = map(int, input().split())
    q = deque()
    v = [0] * 1000001
    print("#{} {}".format(t+1, bfs((N,0))))





