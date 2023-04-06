c, h = map(int, input().split())
ups = [input().split(':') for _ in range(c)]
downs = [input().split(':') for _ in range(h)]
timeline = [0] * (68400)
def make_seconds(time):
    h, m, s = time
    return 3600 * int(h) + 60 * int(m) + int(s) - 18000
for up in ups:
    now = make_seconds(up)
    for i in range(now, now+40):
        timeline[i] = 1
for down in downs:
    now = make_seconds(down)
    for i in range(now, now+40):
        timeline[i] = 1
print(86400 - sum(timeline))