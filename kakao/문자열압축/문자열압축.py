def solution(s):
    result = []
    length = len(s)
    if length == 1:
        return 1
    else:
        for k in range(1, length // 2 + 1):
            blocks = s[:k]
            rep = ''
            cnt = 1
            i = 0
            while (i + 2 * k) <= length:
                left = s[i:i + k]
                right = s[i + k:i + 2 * k]
                if left == right:
                    cnt += 1
                else:
                    blocks += right
                    if cnt != 1:
                        rep += str(cnt)
                    cnt = 1
                i += k
            if cnt != 1:
                rep += str(cnt)
            if i + k != length:
                if right in blocks:
                    blocks += s[i + k:]
                else:
                    blocks += s[i:]
            result.append(len(blocks) + len(rep))
        return min(result)

