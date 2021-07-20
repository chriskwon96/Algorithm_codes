def grouping(string):
    empty_group = dict()
    for i in range(len(string)-1):
        ele = string[i:i+2]
        # print(ele)
        if ele.isalpha():
            if ele in empty_group:
                empty_group[ele] += 1
            else:
                empty_group[ele] = 1
    return empty_group




def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()

    group1, group2 = grouping(str1), grouping(str2)
    if not group1 and not group2:
        return 65536

    union, inter = 0, 0

    for key, val in group1.items():
        if key in group2:
            union += max(val, group2[key])
            inter += min(val, group2[key])
        else:
            union += val

    for key, val in group2.items():
        if key not in group1:
            union += val

    return int( 65536 * (inter/union))





str1 = "FRANCE"
str2 = "french"



solution(str1, str2)
