# user_id: 이벤트 응모자 아이디 목록이 담긴 배열, banned_id: 불량 사용자 아이디 목록이 담긴 배열
# user_id - 알파벳 소문자 + 숫자로만 구성
# banned_id - 알파벳 소문자 + 숫자 + '*' 로만 구성
# - '*' 문자를 하나 이상 포함
# 당첨에서 제외되어야 할 제대 아이디 목록의 경우의 수를 구하세요

dfs 로 풀어야 될거 같은데
checked 를 global로 하고


def solution(user_id, banned_id):
    N, M = len(banned_id), len(user_id)
    checked = [0]*M
    cnt = 0
    for j in range(N):
        bad_user = banned_id[j] # 불량 아이디 골라내기
        for k in range(M):
            user = user_id[k] # 유저 아이디 골라내기
            if checked[k] == 0 and len(bad_user) == len(user):
                for i in range(len(bad_user)): # 불량아이디랑 유저 아이디의 모든 자리 확인
                    if bad_user[i] != '*': # '*'가 아닌데
                        if bad_user[i] != user[i]: # 같지 않다면
                            break # 다음 유저확인
                checked[k] = 1



user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]

# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# banned_id = ["*rodo", "*rodo", "******"]
print(solution(user_id, banned_id))






