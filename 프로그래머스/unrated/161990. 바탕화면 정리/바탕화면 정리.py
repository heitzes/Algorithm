def solution(wallpaper):
    minx, miny, maxx, maxy = 100, 100, 0, 0
    r, c = len(wallpaper), len(wallpaper[0])
    position = []
    for i in range(r):
        for j in range(c):
            if wallpaper[i][j] == "#":
                position.append([i, j])
    for pos in position:
        x, y = pos
        minx = min(x, minx)
        miny = min(y, miny)
        maxx = max(x, maxx)
        maxy = max(y, maxy)
    
    return [minx, miny, maxx+1, maxy+1]