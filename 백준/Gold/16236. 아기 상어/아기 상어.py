from collections import deque
import heapq
n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
def find_baby(n):
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 9: 
                maps[i][j] = 0
                return [i, j]

def bfs(n):
    sx, sy = find_baby(n)
    hq, vi = [], set([(sx, sy)])
    heapq.heappush(hq, [0, sx, sy, 2, 0])
    # hq, vi = deque([[0, sx, sy, 2, 0]]), set([(sx, sy)])
    answer = 0
    while hq:
        hlen = len(hq)
        find = False
        for _ in range(hlen):
            cnt, x, y, shark, eat = heapq.heappop(hq)
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if not (0<=nx<n and 0<=ny<n): continue
                if (nx, ny) not in vi:
                    isFish = maps[nx][ny]
                    if isFish==0 or isFish == shark:
                        vi.add(tuple((nx, ny)))
                        heapq.heappush(hq, [cnt+1, nx, ny, shark, eat])
                    elif isFish < shark:
                        find = True
                        if eat + 1 == shark:
                            heapq.heappush(hq, [cnt+1, nx, ny, shark+1, 0])
                        else:
                            heapq.heappush(hq, [cnt+1, nx, ny, shark, eat+1])  
        while find and hq:
            cnt, x, y, shark, eat = heapq.heappop(hq)
            if maps[x][y] != 0 and maps[x][y] < shark:
                answer += cnt
                hq, vi = [], set([(x, y)])
                heapq.heappush(hq, [0, x, y, shark, eat])
                maps[x][y]= 0
                break
    return answer
print(bfs(n)) 