
T = int(input())
for t in range(1, T+1):
    dec = float(input())
    i = 0.5
    ans = ''
    while dec:
        if dec >= i:
            ans += '1'
            dec -= i
        else:
            ans += '0'
        if len(ans) >= 13:
            ans = 'overflow'
            break
        i /= 2
    print('#{} {}'.format(t,ans))

