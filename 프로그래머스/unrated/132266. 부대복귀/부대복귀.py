from collections import defaultdict
from collections import deque
def bfs(gp, n, sources, wait):
    vi = set()
    res = [200000] * (n+1) 
    res[wait[0]] = 0
    while wait:
        node = wait.popleft()
        vi.add(node)
        for ch in gp[node]:
            if ch not in vi: # 여기서 ch를 방문했는지 확인하니까
                res[ch] = min(res[ch], res[node]+1)
                # if ch not in set(wait): 이 연산을 하지 않아도 됨..!
                wait.append(ch)
    return res
    
def solution(n, roads, sources, destination):
    '''
    가중치가 1인 최단거리 -> bfs/dfs로 풀 수 있다
    인접 리스트로 그래프 구현
    '''
    answer = []
    graph = defaultdict(set)
    for a, b in roads:
        graph[a].add(b)
        graph[b].add(a)
    result = bfs(graph, n, sources, deque([destination]))
    for src in sources:
        if result[src] == 200000:
            answer.append(-1)
        else:
            answer.append(result[src])
    return answer