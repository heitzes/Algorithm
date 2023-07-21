n, s = map(int, input().split())
nlist = list(map(int, input().split()))
answer = 0
def recursive(i, summ):
    global answer
    if i == n:
        if len(summ) > 0 and sum(summ) == s:
            answer += 1
        return
    recursive(i+1, summ)
    recursive(i+1, summ + [nlist[i]])
recursive(0, [])
print(answer)