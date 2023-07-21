import sys
sys.setrecursionlimit(5000)
def solution(n, m, x, y, r, c, k):
    dx, dy = [1, 0, 0, -1], [0, -1, 1, 0]
    answer = 0
    found = False
    alpha = {0: 'd', 1: 'l', 2: 'r', 3: 'u'}
    def dfs(x, y, move):
        nonlocal answer, found
        if len(move) == k:
            if (x, y) == (r-1, c-1):
                found = True
                answer = ''.join(move)
            return answer
        for i in range(4):
            if found: break
            nx, ny = x + dx[i], y + dy[i]
            if not (0<=nx<n and 0<=ny<m): continue
            distance = abs(nx-(r-1)) + abs(ny-(c-1))
            rem = k - (len(move) + 1)
            if rem < distance or abs(distance - rem) % 2: continue
            answer = dfs(nx, ny, move + [alpha[i]])
        return answer
    dfs(x-1, y-1, [])
    if not answer:
        answer = 'impossible'
    return answer