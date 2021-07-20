N = int(input())
six = '666'
inf = 100000000

for k in range(1, inf):
    if six in str(k):
        N -= 1
        if N == 0:
            break

print(k)
