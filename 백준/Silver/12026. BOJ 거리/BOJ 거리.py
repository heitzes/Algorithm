n = int(input())
street = input()
dp = [1e9] * n
order = {"O": "B", "B": "J", "J": "O"}
dp[-1] = 0
for i in range(len(street)-1, -1, -1):
    for j in range(i-1, -1, -1):
        if order[street[i]] == street[j]:
            dp[j] = min(dp[j], dp[i] + (j-i)**2)
print(dp[0] if dp[0] != 1e9 else -1)