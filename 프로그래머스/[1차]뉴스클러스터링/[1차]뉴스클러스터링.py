import math

def groups(string):
    group = []
    for i in range(len(string)-1):
        if string[i].isalpha() and string[i+1].isalpha():
            group.append(string[i:i+2])
    return group


def solution(str1, str2):
    str1, str2 = str1.upper(), str2.upper()
    group1, group2 = groups(str1), groups(str2)
    print(group1, group2)
    inter, uni = [], []
    for g in group1:
        n1 = group1.count(g)
        if g in group2:
            if g not in inter and g not in uni:
                n2 = group2.count(g)
                if n1 > n2:
                    inter.extend([g]*n2)
                    uni.extend([g]*n1)
                else:
                    inter.extend([g]*n1)
                    uni.extend([g]*n2)
        else:
            uni.extend([g]*n1)


    for g in group2:
        if g not in group1:
            uni.extend([g]*group2.count(g))

    print(inter, uni)
    if not uni:
        return 65536
    else:
        return math.floor(65536 * (len(inter)/len(uni)))




# str1 = 'FRANCE'
# str2 = 'french'


# str1 = 'handshake'
# str2 = 'shake hands'

# str2 = 'aa1+aa2'
# str1 = 'AAAA12'

str1 = 'E=M*C^2'
str2 = 'e=m*c^2'


print(solution(str1, str2))

