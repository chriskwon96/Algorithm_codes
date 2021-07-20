T = int(input())

for t in range(1, T+1):
    stov = list(map(int, input()))
    stov.insert(0,0)
    stand = stov[1] #초기 서는 사람 수
    need = 0
    for i in range(2, len(stov)): #두번째 사람부터
        if stand >= i-1:
            stand += stov[i]
        else:
            need += 1
            stand += 1
            stand += stov[i]
    print("#{} {}".format(t, need))

