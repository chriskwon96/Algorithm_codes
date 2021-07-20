import sys

N = int(sys.stdin.readline())
words = list({sys.stdin.readline().strip('\n') for _ in range(N)})

words.sort()
words.sort(key = len)

for i in words:
    print(i)
