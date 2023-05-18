import sys
from collections import defaultdict, deque
# input = sys.stdin.readline
# 방문한 정점을 알아낸다
def bfs(node):
    vi, dq = set([node]), deque([node])
    while dq:
        dpop = dq.popleft()
        for ch in graph[dpop]:
            if ch not in vi:
                vi.add(ch)
                dq.append(ch)
    return vi
commands, order = [], 1
while True:
    a, b = map(int, input().split())
    if (a, b) == (0, 0):
        break
    commands.append([a, b])
while commands:
    v, e = commands.pop(0)
    cnt = 0
    graph = defaultdict(list)
    for i, j in commands[:e]:
        graph[i].append(j)
        graph[j].append(i)
    visited = set([]) # 중복을 피하기위해 사용
    for k in range(1, v+1):
        if k not in visited:
            vi = bfs(k) # k에서 시작하여 방문한 node들
            edges = sum([len(graph[i]) for i in vi]) // 2 # 간선의 수
            if len(vi)-1 == edges: # 정점수보다 간선수가 하나 적으면 트리임
                cnt += 1
            visited.update(vi) # 트리에 속한 node들은 재방문할 필요 없으니 업데이트
    commands = commands[e:]
    if cnt == 0:
        print("Case {}: No trees.".format(order))
    if cnt == 1:
        print("Case {}: There is one tree.".format(order))
    if cnt > 1:
        print("Case {}: A forest of {} trees.".format(order, cnt))
    order += 1