N, M, L = map(int, input().split())
# N: 사람수 M: max 받는수 L: odd-clock even-counterclock

friends = [0]*N
friends[0] = 1 # 초기에 나는 공을 가지고 있는다
i = 0
passes = 0

while friends[i] < M:
    if friends[i] % 2: #홀수라면
        i += L
        i = i % N
        friends[i] += 1
    else:
        i -= L
        i = i % N
        friends[i] += 1

    passes += 1
print(passes)
