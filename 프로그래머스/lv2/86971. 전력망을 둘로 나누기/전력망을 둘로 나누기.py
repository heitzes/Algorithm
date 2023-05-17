from collections import defaultdict
def make_nodes(vi, graph, nodes, n):
    vi.add(n)
    for ch in graph[n]:
        if ch in vi:
            continue
        # 재귀적으로 탐색 (전위 순회)
        make_nodes(vi, graph, nodes, ch)
        nodes[n] += nodes[ch]
    nodes[n] += 1
    return nodes
def solution(n, wires):
    answer = float('inf')
    graph = defaultdict(list)
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
    nodes = make_nodes(set(), graph, defaultdict(int), 1)
    for av in nodes.values():
        cut = n-av
        answer = min(answer, abs(cut-av))
    return answer