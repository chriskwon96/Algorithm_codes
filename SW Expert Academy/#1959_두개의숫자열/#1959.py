
test_cases = int(input())
attempts = 0

while test_cases:
    nums = input().split()
    n = int(nums[0])
    m = int(nums[1])
    diff = abs(n - m)
    sums = []

    Ai = input()
    Ai = Ai.split()  # ['1','3','5']
    Bj = input()
    Bj = Bj.split()  # ['1','3','5']

    if n > m:

        for i in range(diff + 1):
            mults = 0
            for j in range(m):
                mults += int(Ai[j + i]) * int(Bj[j])

            sums.append(mults)

    else:
        for i in range(diff + 1):
            mults = 0
            for j in range(n):
                mults += int(Ai[j]) * int(Bj[j + i])

            sums.append(mults)

    attempts += 1
    print('#{} {}'.format(attempts,max(sums)))
    test_cases -= 1


