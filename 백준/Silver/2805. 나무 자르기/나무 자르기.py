n, m = list(map(int, input().split()))
trees = list(map(int, input().split()))
left, right = 0, max(trees)
while left <= right:
    ans = 0
    cut = (left+right)//2
    for i in trees:
        if i > cut:
            ans += i - cut
    if ans >= m:
        left = cut + 1
    else:
        right = cut - 1
print(right)