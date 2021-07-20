from collections import deque

def bfs():
    q.append([N,0])
    stairs[N] = 0
    while q:
        here, time = q.popleft()
        if here == K:
            return time
        else:
            walk(here, time)
            teleport(here, time)

def walk(here, time):
    if here+1 < 100001 and (stairs[here+1] == -1 or time<stairs[here+1]): #처음 가본 곳이거나 이전에 갔던거보다 더 빨리 간 경우
        stairs[here+1] = time+1
        q.append([here+1, time+1])
    if here-1>=0 and (stairs[here-1] == -1 or time<stairs[here-1]):
        stairs[here-1] = time+1
        q.append([here-1, time+1])

def teleport(here, time):
    if 2*here < 100001 and (stairs[2*here] == -1 or time<stairs[2*here]):
        stairs[2*here] = time+1
        q.append([2*here, time+1])



N, K = map(int, input().split())

stairs = [-1]*100001

q= deque()

print(bfs())

