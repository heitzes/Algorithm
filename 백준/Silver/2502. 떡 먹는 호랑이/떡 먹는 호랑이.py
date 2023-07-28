d, k = map(int, input().split())
dp = [[1,0], [0,1]]
for i in range(2, d):
    dp.append([dp[-2][0] + dp[-1][0], dp[-2][1] + dp[-1][1]])
def solution():
    for i in range(1, k//dp[-1][0]+1):
        for j in range(1, k//dp[-1][1]+1):
            if dp[-1][0] * i + dp[-1][1] * j == k:
                print(i)
                print(j)
                return
solution()