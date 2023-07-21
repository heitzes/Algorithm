from collections import defaultdict
def postOrder(vi, graph, nodes, n):
    vi.add(n)
    for ch in graph[n]:
        if ch in vi:
            continue
        # 재귀적으로 leaf node를 탐색 (후위 순회)
        postOrder(vi, graph, nodes, ch)
        nodes[n] += nodes[ch]
    nodes[n] += 1
    return nodes
def solution(n, wires):
    answer = float('inf')
    graph = defaultdict(list)
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
    nodes = postOrder(set(), graph, defaultdict(int), 1)
    for av in nodes.values():
        cut = n-av
        answer = min(answer, abs(cut-av))
    return answer