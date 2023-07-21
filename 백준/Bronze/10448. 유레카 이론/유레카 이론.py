n = int(input())
check = [int(input()) for _ in range(n)]
triangle = [0]
maxi = max(check)
start = 1
while True:
    if triangle[-1] >= maxi:
        break
    triangle.append(triangle[-1] + start)
    start += 1
triangle.pop(0)
def isTri(n):
    for i in triangle:
        for j in triangle:
            for k in triangle:
                if i + j + k == n:
                    return 1
    return 0
for number in check:
    print(isTri(number))