import sys
def input():
    return sys.stdin.readline()
from itertools import permutations
n = int(input())
nlist = [list(map(int, input().split())) for _ in range(n)]

"""
이닝은 3아웃이 발생하면 종료된다 4,5,6 (0,0,0)
타순은 이닝이 변경되어도 순서를 유지해야한다 7부터시작
안타: 모두 += 1
2루타: 모두 += 2
3루타: 모두 += 3
홈런: 모두 += 4
아웃: 
"""

def calc(order):
    global n
    ind, point = 0, 0
    for ining in nlist:
        b1, b2, b3 = 0, 0, 0
        out = 0
        while out != 3:
            if ining[order[ind]] == 0:
                out += 1
            elif ining[order[ind]] == 4:
                point += (b1 + b2 + b3 + 1)
                b1, b2, b3 = 0, 0, 0
            elif ining[order[ind]] == 3:
                point += (b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 1
            elif ining[order[ind]] == 2:
                point += (b2 + b3)
                b1, b2, b3 = 0, 1, b1
            elif ining[order[ind]] == 1:
                point += (b3)
                b1, b2, b3 = 1, b1, b2
            ind = (ind + 1) % 9
    return point

ans = 0
for order in permutations([1,2,3,4,5,6,7,8]):
    ans = max(ans, calc(list(order[:3])+[0]+list(order[3:])))
print(ans)