import itertools


ops = ['+', '-', '*', '/']


N = int(input())
nums = list(map(int, input().split()))
num_op = list(map(int, input().split()))
my_ops = [ops[0]]*num_op[0] + [ops[1]]*num_op[1] + [ops[2]]*num_op[2] + [ops[3]]*num_op[3]


min_val = 10**9
max_val = -10**9

perm = set(itertools.permutations(my_ops, len(my_ops)))

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

    if total < min_val:
        min_val = total
    if total > max_val:
        max_val = total

print(max_val)
print(min_val)

