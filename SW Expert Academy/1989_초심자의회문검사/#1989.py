
attempts = 0

tries = int(input())

while tries:
    word = input()
    if word == word[::-1]:
        result = 1
    else:
        result = 0

    attempts += 1

    print('#{} {}'.format(attempts, result))
    tries -= 1

