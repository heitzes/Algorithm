n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
cand = [[(i,0), n-i] for i in range(n-1,-1,-1)]
cand.extend([[(0,i), n-i] for i in range(1, n)])
pos = [[] for _ in range(2*n-1)]
for idx, c in enumerate(cand):
    start, num = c
    pos[idx].extend([[start[0]+i, start[1]+i] for i in range(num) if maps[start[0]+i][start[1]+i]])
answer = 0
sums, subs = [0] * (2*n-1), [0] * (2*n-1)
def bruteforce(idx, cnt):
    global n, answer
    if idx == 2*n-1:
        answer = max(answer, cnt)
        return
    flag = False
    for i in range(len(pos[idx])):
        x, y =  pos[idx][i][0], pos[idx][i][1]
        if not sums[x+y] and not subs[x-y]:
            sums[x+y], subs[x-y] = 1, 1
            flag = True
            bruteforce(idx+1, cnt+1)
            sums[x+y], subs[x-y] = 0, 0
    if not flag:
        bruteforce(idx+1, cnt)
    return
bruteforce(0, 0)
print(answer)