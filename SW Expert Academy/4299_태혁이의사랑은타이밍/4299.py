T = int(input())
D0 = H0 = M0 = 11
for t in range(1, T+1):
    result = 0
    D, H, M = map(int, input().split())
    if (D<D0) or (D==D0 and H<H0) or (D==D0 and H==H0 and M<M0):
        result = -1
    else:
        result += (D-D0)*24*60 + (H-H0)*60 + (M-M0)

    print('#{} {}'.format(t, result))