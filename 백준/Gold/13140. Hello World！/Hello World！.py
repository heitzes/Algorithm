from itertools import permutations
n = int(input())
wlist = [i for i in range(10)]
def calc(perm):
    h, e, l, o, w, r, d = perm
    if h == 0 or w == 0:
        return 0
    hello = str(h) + str(e) + str(l) + str(l) + str(o)
    world = str(w) + str(o) + str(r) + str(l) + str(d)
    ans = int(hello) + int(world)
    if ans == n:
        print("  {}".format(hello))
        print("+ {}".format(world))
        print("-------")
        print(" "*(7-len(str(n))) + str(n))
        return 1
    return 0

def solution():
    for p in permutations(wlist, 7):
        k = calc(p)
        if k == 1: return
    print("No Answer")
    return
solution()