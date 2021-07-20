T = int(input())
for t in range(1, T+1):
    N = int(input())
    happydays = []
    cnt = 0
    for _ in range(N):
        happydays.append(int(input()))
    check = [1] + [0]*(len(happydays)-1)

    while not(all(check)): #check 안에 0이 존재할 경우:
        i = 1
        while i < len(happydays):
            if check[i] == 0: #check 안된애를 발견
                cnt += 1
                sub = happydays[i] - happydays[0] # 차를 찾아
                for j in range(i, len(happydays)):
                    if happydays[j] % sub == 1:
                        check[j] = 1
            else:
                i += 1

    print('#{} {}'.format(t, cnt))
