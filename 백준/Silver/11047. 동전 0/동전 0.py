n, money = map(int, input().split())
coins = [int(input()) for _ in range(n)][::-1]
ans = 0
for coin in coins:
    if money == 0: break
    if coin > money: continue
    use = money // coin
    money -= use * (coin)
    ans += use
print(ans)