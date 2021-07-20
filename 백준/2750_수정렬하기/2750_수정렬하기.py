N = int(input())
nums = [int(input()) for _ in range(N)]

# bubble sort
for i in range(N-1):
    for j in range(N-i-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
for i in nums:
    print(i)
