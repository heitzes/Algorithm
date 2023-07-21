import sys
from collections import Counter
def input():
    return sys.stdin.readline().rstrip()
n, m = map(int, input().split())
nlist = list(map(int, input().split()))
preSum = [0] * (n+1)
for i in range(n):
    preSum[i+1] = (preSum[i] + nlist[i]) % m
count = Counter(preSum)
answer = 0
for i in range(m):
    answer += (count[i] * (count[i]-1))//2
print(answer)