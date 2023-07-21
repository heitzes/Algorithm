from collections import defaultdict
def compare(w, c):
    count = [1 for i in range(len(w)) if w[i] != c[i]]
    if sum(count) == 1:
        return 1
    return 0
def dfs(gp, bg, tg, vi, node, alist):
    """
    dfs로 gp를 탐색하며 bg에서 tg까지 도달하는데 걸리는 경로를 측정하고, 최단거리를 찾는다
    """
    vi.append(node)
    if node == tg:
        alist.append(len(vi)-1)
        return
    for child in gp[node]:
        if child not in vi:
            dfs(gp, bg, tg, vi, child, alist) # 재귀적으로 dfs
            vi.pop() # 백트랙킹
    return alist
def solution(begin, target, words):
    """
    그래프: 객체간의 관계를 표현하는 자료구조 정점과 간선으로 이루어짐
    hit, hot 사이의 간선 가중치는 1 
    hit, dot 사이의 간선 가중치는 2 -> 무시
    hit, dog 사이의 간선 가중치는 3 -> 무시
    ...
    begin과 words 안의 단어 사이의 관계를 인접리스트 그래프로 표현
    단, words 안에 target이 없으면 바로 0를 return
    """
    if target not in words:
        return 0
    words = [begin] + words
    graph = defaultdict(list)
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if compare(words[i], words[j]):
                graph[words[i]].append(words[j])
                graph[words[j]].append(words[i])
    return min(dfs(graph, begin, target, [], begin, []))  
