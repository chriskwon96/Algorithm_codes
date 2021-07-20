import sys
N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]

keys = [0]*8001
#
# for _ in range(N):
#     keys[int(sys.stdin.readline())+4000] += 1

vals = [0]*8001
maxes = -1
#산술평균
print(round(sum(nums)/N))
# for i in range(8001):

#중앙값
nums.sort()
print(nums[(N-1)//2])

#최빈값-최빈값이 여러개면 최빈값중 두번째로 작은 값

for i in nums:
    keys[i] = i
    vals[i] += 1
cnt = 0
maxes = max(vals)
flag = 0
for i in range(8001):
    if vals[i] == maxes:
        cnt += 1
        if cnt == 2:
            flag = 1
            a= i
            break


if flag:
    print(a-4000)
else:
    print(vals.index(maxes)-4000)

#범위
print(nums[-1]-nums[0])