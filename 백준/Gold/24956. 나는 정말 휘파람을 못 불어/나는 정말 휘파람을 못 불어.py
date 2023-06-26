n = int(input())
word = input()
wlist, hlist = [], []
edp = [0] * (n+1)
wdp = [0] * (n+1)
for i in range(n-1, -1, -1):
    edp[i] = edp[i+1] + (1 if word[i] == "E" else 0)
for j in range(1, n+1):
    wdp[j] = wdp[j-1] + (1 if word[j-1] == "W" else 0)
answer = 0
for k in range(n):
    if word[k] == "H":
        answer += (wdp[k]) * (2**(edp[k])-(1+edp[k])) % (1000000007)
print(answer % (1000000007))