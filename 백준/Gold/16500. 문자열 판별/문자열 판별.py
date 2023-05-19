string = input()
n = int(input())
wset = set([input() for _ in range(n)])
dp = [0] * (len(string)+1)
dp[0] = 1
for i in range(len(string)):
    if dp[i] != 1:
        continue
    for word in wset:
        if string[i:i+len(word)] == word:
            dp[i+len(word)] = 1
print(dp[-1])