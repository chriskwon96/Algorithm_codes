from _collections import deque

def bfs(q):
    while q:
        node, cnt = q.popleft()
        v[node] = 1
        cand = [node+1, node-1, node*2, node-10]
        for new in cand:
            if new == M:
                return cnt+1
            else:
                if (0 < new <= 1000000) and (v[new] == 0):
                    v[new]=1
                    q.append((new, cnt+1))
                    
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    q = deque()
    q.append((N, 0))
    v = [0]*1000001
    print('#{} {}'.format(t, bfs(q)))