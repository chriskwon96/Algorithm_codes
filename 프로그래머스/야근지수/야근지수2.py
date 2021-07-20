import heapq

def solution(n, works):
    N = len(works)
    total = 0
    for i in range(len(works)):
        works[i] = -works[i]
    heapq.heapify(works)

    while n and any(works):
        heapq.heappush(works, heapq.heappop(works)+1)
        n -= 1

    
    for i in range(N):
        total += works[i] ** 2
    return total



