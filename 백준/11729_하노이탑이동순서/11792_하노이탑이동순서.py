import copy
def hanoi(N):
    if N == 1:
        return [[1,3]]
    else:
        a = hanoi(N-1)
        for i in range(len(a)):
            for j in range(2):
                if a[i][j] == 2:
                    a[i][j] = 3
                elif a[i][j] == 3:
                    a[i][j] = 2
        final = a + [[1,3]]
        b = copy.deepcopy(a)
        for i in range(len(b)):
            for j in range(2):
                if b[i][j] == 1:
                    b[i][j] = 2
                elif b[i][j] == 3:
                    b[i][j] = 1
                else:
                    b[i][j] = 3
        final += b
        return final

N = int(input())
result = hanoi(N)
print(len(result))
for i in result:
    for j in i:
        print(j, end = ' ')
    print()
