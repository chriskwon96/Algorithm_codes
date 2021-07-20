T = int(input())

for t in range(1, T+1):
    nums = list(map(int, input().split()))
    if " " in nums:
        nums.remove(" ")
    nums.sort()
    nums.pop()
    nums.pop(0)
    avg = round(sum(nums)/8)
    print('#{} {}'.format(t, avg))