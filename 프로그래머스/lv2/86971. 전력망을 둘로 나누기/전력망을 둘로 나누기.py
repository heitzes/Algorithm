from collections import defaultdict
def make_tree(vi, graph, tree, nodes, n):
    vi.add(n)
    for ch in graph[n]:
        if ch in vi:
            continue
        tree[n].append(ch)
        make_tree(vi, graph, tree, nodes, ch)
        nodes[n] += nodes[ch]
    nodes[n] += 1
    return tree, nodes
def solution(n, wires):
    answer = float('inf')
    graph = defaultdict(list)
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
    tree, nodes = make_tree(set(), graph, defaultdict(list), defaultdict(int), 1)
    available = set(nodes.values())
    for av in available:
        cut = n-av
        answer = min(answer, abs(cut-av))
    return answer