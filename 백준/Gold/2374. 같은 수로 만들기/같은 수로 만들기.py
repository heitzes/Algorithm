n = int(input())
nlist = [int(input()) for _ in range(n)]
maxi = max(nlist)
nlist.append(maxi)
answer = 0
stack = []
for num in nlist:
    if stack:
        if stack[-1] <= num:
            answer += (num - stack[-1])
            while stack and stack[-1] <= num:
                stack.pop()
        stack.append(num)
        continue
    stack.append(num)
print(answer)