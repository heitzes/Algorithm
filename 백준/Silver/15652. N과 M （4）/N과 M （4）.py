n, m = map(int, input().split())
nlist = [i for i in range(1, n+1)]
def recursive(string):
    if len(string) == m+1:
        print(' '.join(string[1:]))
        return
    for k in range(1, n+1):
        if k >= int(string[-1]):
            recursive(string + str(k))
recursive('0')