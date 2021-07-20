T= int(input())

for t in range(1, T+1):
    num= input()
    cnt = 0
    if int(num[0]) == 1:
        cnt+=1

    for i in range(len(num)-1):
        if num[i] != num[i+1]:
            cnt+=1

    print('#{} {}'.format(t,cnt))

