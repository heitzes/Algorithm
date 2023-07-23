n = int(input())
string = input()
wind, eind, hind = [], [], []
for i in range(n):
    if string[i] == "H":
        hind.append(i)
    if i == 0:
        wind.append(0)
        continue
    if string[i-1] == "W":
        wind.append(wind[-1] + 1)
    else:
        wind.append(wind[-1])
for i in range(n-1, -1, -1):
    if i == n-1:
        eind.append(0)
        continue
    if string[i+1] == "E":
        eind.append(eind[-1] + 1)
    else:
        eind.append(eind[-1])
eind = eind[::-1]
answer = 0
for h in hind:
    k = eind[h]
    answer += wind[h] * (2 ** (k) - (1+k))
print(answer % 1000000007)