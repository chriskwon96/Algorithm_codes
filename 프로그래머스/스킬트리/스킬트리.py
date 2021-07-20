
def solution(skill, skill_trees):
    ans = 0
    for tree in skill_trees:
        i = 0
        flag = 1
        for t in tree:
            if t in skill:
                if t == skill[i]:
                    i += 1
                    if i == len(skill):
                        break
                else:
                    flag = 0
                    break

        if flag:
            # print(tree)
            ans += 1



    return ans





print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))






