a = [[0,5],[2,4],[0,3]]

a.sort(key=lambda ele:ele[1])
a.sort(key=lambda ele:ele[0])
print(a)