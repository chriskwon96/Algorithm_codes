
for t in range(10):
    T = int(input())
    target_str = input()
    given_str = input()
    cnt = 0

    for i in range(len(given_str) - len(target_str)+1):
        if target_str == given_str[i:i+len(target_str)]:

            cnt += 1

    print('#{} {}'.format(T, cnt))
