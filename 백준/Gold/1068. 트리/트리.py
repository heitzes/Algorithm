N = int(input())
inplist = [int(i) for i in input().split(' ')]
node_list = []
class Node:
    def __init__(self,val):
        self.val = val
        self.parent = None
        self.child = []
        
if N <= 50 and N>=1:
    for i in range(len(inplist)):
        node_list.append(Node(i))

for i in range(len(inplist)):
    if inplist[i]!=-1:
        node_list[i].parent = node_list[inplist[i]]
        node_list[inplist[i]].child.append(node_list[i])

rem = int(input())
visited = [node_list[rem]]
bref = []
def BFS(node):
    ref_list = [node_list[rem].val]
    bref = [node_list[rem]]
    while len(ref_list) != 0:
        a =node_list[ref_list[0]].child
        for i in a:
            if i not in visited:
                visited.append(i)
                ref_list.append(i.val)
        ref_list.remove(ref_list[0])

BFS(node_list[rem])

ncopy = node_list.copy()

if node_list[rem].parent != None:
    node_list[rem].parent.child.remove(node_list[rem])
    node_list[rem].parent = None
else:
    pass
    
for i in visited:
    node_list.remove(ncopy[i.val])

cnt = 0
for i in node_list:
    if len(i.child)==0:
        cnt +=1
print(cnt)