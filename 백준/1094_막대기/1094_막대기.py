X = int(input())
x = 0
cnt = 0
while x < X:
    for i in range(6, -1, -1): #6부터 0까지
        if (1<<i) <= X-x:
            x += (1<<i)
            cnt += 1
            if x == X:
                print(cnt)
