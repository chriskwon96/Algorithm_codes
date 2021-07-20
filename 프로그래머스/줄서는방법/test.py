
def f(n,k):
    if n == k :
        return p
    else:
        for i in range(k):
            if v[i] == 0 :
                v[i] = 1
                p[n] = A[i]
                f(n+1, k)
                v[i] = 0




A = list(range(1, 4))
v = [0] * 3
p = [0] * 3

print(f(0,3))

