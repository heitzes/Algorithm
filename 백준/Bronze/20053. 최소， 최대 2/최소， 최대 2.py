n = int(input())
for _ in range(n):
    m = int(input())
    mlist = list(map(int, input().split()))
    print("{} {}".format(min(mlist), max(mlist)))