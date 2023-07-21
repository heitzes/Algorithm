n = int(input())
arr = [-1] * (11)
answer = 0
for _ in range(n):
    cow, pos = map(int, input().split())
    if arr[cow] == -1:
        arr[cow] = pos
    else:
        if pos != arr[cow]:
            answer += 1
            arr[cow] = pos
print(answer)