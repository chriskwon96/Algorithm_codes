T = int(input())

for t in range(1, T+1):
    print('#{}'.format(t))
    N = int(input())
    alpha = [0]*N
    nums =[0]*N
    for i in range(N):
        a, num = input().split()
        num = int(num)
        alpha[i] = a
        nums[i] = num

    i = 0
    doc = 10
    while i < N:
        if nums[i] > doc:
            print(alpha[i]*doc)
            nums[i] = nums[i] - doc
            doc = 10
        elif nums[i] < doc:
            print(alpha[i]*nums[i], end = '')
            doc = doc - nums[i]
            nums[i] = 0
            i += 1
        else:
            print(alpha[i]*doc)
            nums[i] = 0
            i += 1
            doc = 10
    print()
