p = input()

def solution(p):
    opened, closed = 0, 0
    if not p:
        return ""
    else:
        for i in range(len(p)):
            if p[i] == '(':
                opened += 1
            else:
                closed += 1
            if opened == closed:
                u = p[:i + 1]
                v = p[i + 1:]
                break

        if check(u):
            if v: #u가 올바른 문자열이고 v가 비어있지 않다면
                solution(v) #다시 u,v로 쪼개자
            else:
                return u
        else: #u가 올바른 문자열이 아니라면
            fix_u = u[1:-1]
            print(fix_u)
            for j in range(len(fix_u)):
                if fix_u[j] == '(':
                    fix_u[j] = ')'
                else:
                    fix_u = '('
            return('('+solution(v)+')'+fix_u)




def check(my_string):
    stack = []
    my_string = list(my_string)
    while my_string:

        if my_string[0] == '(':
            stack.append(my_string.pop(0))
        else:
            if stack:
                my_string.pop(0)
                stack.pop()
            else:
                return 0 #올바르지 않은괄호
    return 1 #올바른 괄호




print(solution(p))