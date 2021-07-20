
T= int(input())

for t in range(1,T+1):
    s1,s2,s3 = map(int, input().split())

    if s1 == s2 == s3: # 3sides same
        result = s1

    else:
        if s1 == s2:
            result = s3
        elif s1 == s3:
            result = s2
        else:
            result = s1
    print('#{} {}'.format(t, result))
