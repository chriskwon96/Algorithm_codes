def pivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return pivo(n-1) + pivo(n-2)

N = int(input())
print(pivo(N))