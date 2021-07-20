import sys


N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]


keys = [0]*N
#
# for _ in range(N):
#     keys[int(sys.stdin.readline())+4000] += 1

vals = [0]*N
maxes = []
#산술평균
print(round(sum(nums)/N))
# for i in range(8001):

#중앙값
nums.sort()
print(nums[(N-1)//2])

#최빈값-최빈값이 여러개면 최빈값중 두번째로 작은 값
for i in range(N):
    if nums[i] not in keys:
        keys[i] = nums[i]
        vals[i] = 1
    else:
        vals[keys.index(nums[i])] += 1

flag = 0
for i in range(len(keys)):
    if vals[i] == max(vals):
        maxes.append(keys[i])
        if len(maxes) == 2:
            flag = 1
            break

if flag:
    print(maxes[1])
else:
    print(maxes[0])


#범위
print(nums[-1]-nums[0])