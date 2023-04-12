from collections import Counter
sentence = input()
slen = len(sentence)
nword = int(input())
available = list()
words = list()
for _ in range(nword):
    word = input()
    available.append(Counter(word))
    words.append(word)

def calculate(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    return cnt

cost_dp = [[float('inf') for _ in range(slen-i+1)] for i in range(slen)]
for i in range(slen):
    for j in range(i+1, slen+1):
        for av, w in zip(available, words):
            if Counter(sentence[i:j]) == av:
                cost_dp[i][j-i] = min(cost_dp[i][j-i], calculate(sentence[i:j], w))

dp = [float('inf') for _ in range(slen+1)]
dp[0] = 0
for n in range(1,slen+1):
    for k in range(n):
        dp[n] = min(dp[k] + cost_dp[k][n-k], dp[n])
if dp[-1] != float('inf'):
    print(dp[-1])
else:
    print(-1)