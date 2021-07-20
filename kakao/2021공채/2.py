# 2<= orders <= 20
# orders의 원소의 크기 2이상 10이하, 중복x , 대문자
# course크기 1<= <=10, 원소는 오름차수능로 2이상 10 이하, 중복 x
# 사전순으로 return
from itertools import combinations


def solution(orders, course):
    ans = []
    for menu_num in course:
        my_dict = dict()
        for order in orders:
            if len(order) < menu_num:
                continue
            for comb in combinations(order, menu_num):
                comb_str = "".join((sorted(comb)))
                if comb_str in my_dict:
                    my_dict[comb_str] += 1
                else:
                    my_dict[comb_str] = 1

        # print(my_dict)
        if my_dict:
            max_val = max(my_dict.values())
            if max_val < 2:
                continue
        # print(my_dict)
        for key, val in my_dict.items():
            if val == max_val:
                ans.append(key)


    ans.sort()
    return ans







# orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# course = [2,3,4]
#
orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]

# orders = ["XYZ", "XWY", "WXA"]
# course = [2,3,4]

print(solution(orders, course))