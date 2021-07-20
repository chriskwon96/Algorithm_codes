
def square(n, start_i, start_j, num):
    global ans, r ,c
    if n == 0:
        ans = num
    else:
        interval = 2**(n-1)
        if start_i<=r<start_i+interval:
            if start_j<=c<start_j+interval: # top-left
                square(n-1, start_i, start_j, num)
            else: # top-right
                square(n-1, start_i, start_j+interval, num+interval**2)

        else:
            if start_j<=c<start_j+interval: # bottom-left
                square(n-1, start_i+interval, start_j, num +2*(interval**2))
            else: # bottom-right
                square(n-1, start_i+interval, start_j+interval, num + 3*(interval**2))


N, r, c = map(int, input().split())

square(N, 0,0,0)

print(ans)








