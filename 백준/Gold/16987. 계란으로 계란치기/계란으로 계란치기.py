n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def check():
    answer = 0
    for egg in eggs:
        if egg[0] <= 0: answer += 1
    return answer

def backtrack(idx):
    global n, ans
    if idx == n:
        ans = max(ans, check())
        return
    if eggs[idx][0] <= 0:
        backtrack(idx+1)
    for i in range(n):
        if i != idx and eggs[i][0] > 0 and eggs[idx][0] > 0:
            eggs[i][0] -= eggs[idx][1]
            eggs[idx][0] -= eggs[i][1]
            backtrack(idx + 1)
            eggs[idx][0] += eggs[i][1]
            eggs[i][0] += eggs[idx][1]
    else:
        backtrack(n)
backtrack(0)
print(ans)