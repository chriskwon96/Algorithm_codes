T = int(input())

for t in range(1,T+1):
    h1, m1, h2, m2 = map(int, input().split())
    hours = 0
    minutes = 0
    minutes = (m1+m2) % 60
    hours = (m1+m2) // 60 + h1 + h2
    if hours % 12 == 0:
        hours = 12
    else:
        hours = hours % 12

    print('#{} {} {}'.format(t, hours, minutes))
