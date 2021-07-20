import sys

N = int(sys.stdin.readline())
n = N//10
while n < N:
    gen = list(map(int, str(n)))
    total = sum(gen) + n
    if total == N:
        result = ''.join(map(str, gen))
        break
    n += 1
    if n== N:
        result = 0
        break
print(result)
