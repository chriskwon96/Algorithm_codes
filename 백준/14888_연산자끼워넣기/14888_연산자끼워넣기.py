
global p
ops = ['+', '-', '*', '/']


def f(n, k): #n:순열의 n번 원소
    if n == k:
        perm.add(tuple(p))

    else:
        for i in range(k):
            if used[i] == 0:  #i번 원소가 사용되지 않았으면
                used[i] = 1 #사용함으로 표시
                p[n] = my_ops[i]
                f(n+1, k) #n+1 원소
                used[i] = 0

N = int(input())
nums = list(map(int, input().split()))
num_op = list(map(int, input().split()))
my_ops = [ops[0]]*num_op[0] + [ops[1]]*num_op[1] + [ops[2]]*num_op[2] + [ops[3]]*num_op[3]

perm = set()
result = []

used = [0] * len(my_ops)
p = [0] * len(my_ops)
f(0, len(my_ops))

for per in perm:
    stack = nums[:]
    pp = list(per)
    while pp:
        a = stack.pop(0)
        b = stack.pop(0)
        op = pp.pop(0)

        if op == '+':
            total = a + b
        elif op == '*':
            total = a * b
        elif op == '-':
            total = a - b
        else:
            total = int(float(a) / b)

        stack.insert(0, total)
    result.extend(stack)

print(max(result))
print(min(result))
