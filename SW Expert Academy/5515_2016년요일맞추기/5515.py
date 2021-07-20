T = int(input())
dates = [4,5,6,0,1,2,3]
days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for t in range(1, T+1):
    M, D = map(int, input().split())
    gap = sum(days[1:M])
    gap += (D-1)
    date = dates[gap % 7]
    print('#{} {}'.format(t, date))
