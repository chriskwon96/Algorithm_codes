
given = int(input())
attempt=0

while given:
    N = int(input())
    result = 0

    for i in range(1, N + 1):
        result += -((-1) ** i) * i

    given -= 1
    attempt+=1

    print('#{} {}'.format(attempt, result))


