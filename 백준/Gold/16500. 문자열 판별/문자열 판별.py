string = input()
n = int(input())
wlist = [input() for _ in range(n)]
dp = [-1] * (len(string)+1)
def dfs(idx):
    global n
    if dp[idx] != -1:
        return dp[idx]
    dp[idx] = 1
    for word in wlist:
        if string[idx:idx+len(word)] == word:
            dfs(idx + len(word))
    return dp[idx]
dfs(0)
print(dp[-1] if dp[-1]==1 else 0)