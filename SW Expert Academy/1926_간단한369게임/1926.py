threes = ['3','6','9']

N = int(input())
my_list = [0]*(N+1)
for i in range(N+1):
    my_list[i] = str(i)

i = 0
while i < len(my_list):
    cnt = 0
    if ('3' in my_list[i]) or ('6' in my_list[i]) or ('9' in my_list[i]):
        for N in range(len(my_list[i])):
            if my_list[i][N] in threes:
                cnt += 1
        my_list[i] = '-'*cnt
    i += 1

my_list.pop(0)

print('{}'.format(' '.join(my_list)))
