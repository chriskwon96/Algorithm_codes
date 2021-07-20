import math

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
total = 0
for Ai in A:
    if Ai > B:
        Ai -= B
        total += math.ceil(Ai/C)
    total += 1
print(total)


