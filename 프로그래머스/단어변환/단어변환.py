def check(word1, word2, l):
  cnt = 0
  for i in range(l):
    if word1[i] != word2[i]:
      cnt += 1
      if cnt == 2:
        return False
  return True



def f(begin, target, words, ans, v):
  global min_ans
  if ans < min_ans:
    # print("========")
    if check(begin, target, N):
      ans += 1
      if ans < min_ans:
        min_ans = ans
        # print(ans)

    else:
      # print("++++++++")
      for word in words:
        if check(begin, word, N):
          v[words.index(word)] = 1
          f(word, target, words, ans+1, v)
          v[words.index(word)] = 0





def solution(begin, target, words):
  global min_ans, N
  ans = 0
  min_ans = 50
  N = len(begin)
  v = [0]*len(words)
  if target not in words:
    return 0

  f(begin, target, words, 0, v)

  if min_ans == 50:
    return 0
  else:
    return min_ans

# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))

