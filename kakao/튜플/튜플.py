def intoList(s):
    el = ''
    parts = []
    part = []
    # print(s)
    for ss in s:
        if ss.isdigit():
            el += ss
        elif ss == ',' and el:
            part.append(int(el))
            el = ''
        elif ss == '}':
            part.append(int(el))
            parts.append(part)
            part = []
            el = ''
        # print(el, part, parts)
    return parts




def solution(s):
    s = intoList(s[1:-1])
    s.sort(key=len)
    ans = []
    N = len(s)
    for i in range(N):
        p = s[i][0]
        ans.append(p)
        for j in s[i+1:]:
            j.remove(p)

    return ans



s = "{{123}}"
print(solution(s))







