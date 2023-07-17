import sys
def input():
    return sys.stdin.readline().rstrip()
string = input()
m = int(input())
dp = [[0]*(len(string)+1) for _ in range(26)]
for i in range(len(string)):
    dp[ord(string[i])-97][i+1] = 1
for i in range(26):
    for j in range(len(string)):
        dp[i][j+1] += dp[i][j]
for _ in range(m):
    alpha, s, e = input().split()
    print(dp[ord(alpha)-97][int(e)+1] - dp[ord(alpha)-97][int(s)])