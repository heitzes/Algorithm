def blank(s):
    return " " * (s+2)
def verticalR(s):
    return " "*(s+1) + "|"
def verticalL(s):
    return "|" + " "*(s+1)
def verticalLR(s):
    return "|" + " "*(s) + "|"
def horizontal(s):
    return " " + "-"*s + " "
s, n = map(int, input().split())

order = {
    1: [0] + [1] * s + [0] + [1] * s + [0],
    2: [4] + [1] * s + [4] + [2] * s + [4],
    3: [4] + [1] * s + [4] + [1] * s + [4],
    4: [0] + [3] * s + [4] + [1] * s + [0],
    5: [4] + [2] * s + [4] + [1] * s + [4],
    6: [4] + [2] * s + [4] + [3] * s + [4],
    7: [4] + [1] * s + [0] + [1] * s + [0],
    8: [4] + [3] * s + [4] + [3] * s + [4],
    9: [4] + [3] * s + [4] + [1] * s + [4],
    0: [4] + [3] * s + [0] + [3] * s + [4]
}

nlist = list(map(int, list(str(n))))
def select(num, s):
    if num == 0: return blank(s)
    elif num == 1: return verticalR(s)
    elif num == 2: return verticalL(s)
    elif num == 3: return verticalLR(s)
    elif num == 4: return horizontal(s)

for i in range(2*s+3):
    print(' '.join([select(order[k][i], s) for k in nlist]))