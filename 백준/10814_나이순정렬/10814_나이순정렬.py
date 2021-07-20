import sys
from operator import itemgetter

N = int(sys.stdin.readline())
people = [0]*N
for i in range(N):
    x,y = map(str, sys.stdin.readline().split())
    people[i] = (int(x), y)

for person in sorted(people, key=itemgetter(0)):
    for j in person:
        print(j, end = ' ')
    print()

