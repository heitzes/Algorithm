nlist = []
for i in range(100, 1000):
    k = str(i)
    if '0' in k:
        continue
    if len(set(list(k))) == 3:
        nlist.append(k)
n = int(input())
def compare(n, s, b):
    available = set([])
    for num in nlist:
        strike, ball = 0, 0
        for i in range(3):
            if n[i] == num[i]:
                strike += 1
            elif n[i] in num:
                ball += 1
        if (strike, ball) == (s, b):
            available.add(num)
    return available
answer = set(nlist)
for _ in range(n):
    guess, s, b = map(int, input().split())
    answer = answer & (compare(str(guess), s, b)) 
print(len(answer))