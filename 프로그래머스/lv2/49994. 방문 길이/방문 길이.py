def solution(dirs):
    x, y = 0, 0
    vi = set()
    move = {'U': [0, 1], 'D': [0, -1], 'L': [-1, 0], 'R': [1, 0]}
    for cmd in dirs:
        nx, ny = x + move[cmd][0], y + move[cmd][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            vi.add((x, y, nx, ny))
            vi.add((nx, ny, x, y))
            x, y = nx, ny
    return len(vi)//2