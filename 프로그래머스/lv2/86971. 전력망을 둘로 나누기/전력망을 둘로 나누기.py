from collections import defaultdict
def solution(n, wires):
    answer = float('inf')
    graph = defaultdict(list)
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
    vi = set()
    tree = defaultdict(list)
    nodes = defaultdict(int)
    def make_tree(n):
        vi.add(n)
        for ch in graph[n]:
            if ch in vi:
                continue
            tree[n].append(ch)
            make_tree(ch)
            nodes[n] += nodes[ch]
        nodes[n] += 1
    make_tree(1)
    available = set(nodes.values())
    for av in available:
        cut = n-av
        answer = min(answer, abs(cut-av))
    return answer