import sys
def input():
    return sys.stdin.readline().rstrip()
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
n, m, v = map(int, input().split()) 
nlist = list(map(int, input().split()))
nodes = [Node(i) for i in nlist]
for i in range(n-1):
    nodes[i].next = nodes[i+1]
nodes[n-1].next = nodes[v-1]

for _ in range(m):
    q = int(input())
    now = nodes[0]
    if q >= n:
        q = v-1 + (q-(v-1)) % (n-(v-1))
    print(nodes[q].data)