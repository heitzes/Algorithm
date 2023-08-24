def solution(dirs):
    answer = 0
    x, y = 0, 0
    vi = set()
    def move(i, j, c):
        if c == 'U':
            if j + 1 <= 5: return i, j+1
        elif c == 'D':
            if j - 1 >= -5: return i, j-1
        elif c == 'L':
            if i - 1 >= -5: return i-1, j
        elif c == 'R':
            if i + 1 <= 5: return i+1, j
        return i, j
    rcmd = {'U': 'D', 'D':'U', 'L':'R', 'R':'L'}
    for cmd in dirs:
        pos = str(x)+str("*")+str(y)+cmd
        nx, ny = move(x, y, cmd)
        rpos = str(nx)+str("*")+str(ny)+rcmd[cmd]
        if x == nx and y == ny: continue
        if pos not in vi and rpos not in vi:
            answer += 1
            vi.add(pos)
        x, y = nx, ny
    return answer