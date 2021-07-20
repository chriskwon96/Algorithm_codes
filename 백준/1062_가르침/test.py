a = {"a", "b"}
b = {"c","d","a"}
c = {"c","b","a","d"}
# print(c[0], c[1])
print(set(c))
print(bool(b.issubset(c)))
print(len(c))