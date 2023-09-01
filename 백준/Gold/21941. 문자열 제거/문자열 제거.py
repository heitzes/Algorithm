string = input()
n = int(input())
words = dict()
for _ in range(n):
    w, c = input().split()
    words[w] = int(c)
dp = [0] * (len(string)+1)
for leng in range(1, len(string)+1):
    dp[leng] = dp[leng-1] + 1
    for i in range(1, 101):
        if leng - i < 0: break
        suffix = string[leng-i:leng]
        if suffix in words:
            dp[leng] = max(dp[leng], dp[leng-i] + words[suffix])
print(dp[-1])