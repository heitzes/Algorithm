from collections import deque
def solution(maps):
    answer = []
    r, c = len(maps), len(maps[0])
    vi = set()
    
    def bfs(x, y):
        dq = deque([[x, y]])
        vi.add((x,y))
        ans = int(maps[x][y])
        while dq:
            px, py = dq.popleft()
            for dx, dy in [[0,1], [0,-1], [1,0], [-1,0]]:
                cx, cy = px + dx, py + dy
                if 0<=cx<r and 0<=cy<c and (cx, cy) not in vi:
                    if maps[cx][cy] != "X":
                        ans += int(maps[cx][cy])
                        vi.add((cx, cy))
                        dq.append([cx, cy])
        return ans
    
    for i in range(r):
        for j in range(c):
            if maps[i][j] != "X" and (i,j) not in vi:
                answer.append(bfs(i, j))
    if not answer:
        return [-1]
    return sorted(answer)