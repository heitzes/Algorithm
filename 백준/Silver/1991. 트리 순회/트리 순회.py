from collections import defaultdict
n = int(input())
tree = defaultdict(list)
for _ in range(n):
    root, left, right = input().split(" ")
    tree[root].extend([left, right])
p, i, l = [], [], []
def preOrder(node):
    p.append(node)
    left, right = tree[node]
    if left != '.': preOrder(left)
    if right != '.': preOrder(right)
    return ''.join(p)
def inOrder(node):
    left, right = tree[node]
    if left != '.': inOrder(left)
    i.append(node)
    if right != '.': inOrder(right)
    return ''.join(i)
def postOrder(node):
    left, right = tree[node]
    if left != '.': postOrder(left)
    if right != '.': postOrder(right)
    l.append(node)
    return ''.join(l)
print(preOrder('A'))
print(inOrder('A'))
print(postOrder('A'))