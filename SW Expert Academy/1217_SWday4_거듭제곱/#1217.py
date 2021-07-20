
def power(a, b):

    if b == 1:
        return a
    return a*power(a, b-1)

T = 10
for t in range(1, T+1):
    test_case = int(input())
    nums = list(map(int, input().split()))
    a= nums[0]
    b=nums[1]

    print('#{} {}'.format(test_case, power(a,b)))
