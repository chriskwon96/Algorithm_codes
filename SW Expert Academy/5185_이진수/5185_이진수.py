T = int(input())
for t in range(1, T+1):
    N, num = input().split()
    ans=''
    for i in range(int(N)):
        bin_num = bin(int(num[i],16))[2:]
        while len(bin_num) < 4:
            bin_num = '0'+ bin_num
        ans += bin_num
    print('#{} {}'.format(t, ans))






