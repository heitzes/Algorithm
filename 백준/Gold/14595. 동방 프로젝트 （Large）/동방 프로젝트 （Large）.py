n = int(input())
m = int(input())
behavior = []
answer, prevE = 0, 0
for _ in range(m):
    s, e = map(int, input().split())
    behavior.append([s, e])
behavior.sort()
for s, e in behavior:
    if s > prevE:
        answer += (s - prevE)
    prevE = max(e, prevE)
answer += n - prevE
print(answer)