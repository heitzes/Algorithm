w, h, f, c, x1, y1, x2, y2 = map(int, input().split())
nw, nh = max(w-f, f), h//(c+1)
k = min(w-f, f)
if x1 < k < x2:
    sq1 = (k-x1) * (y2-y1) * (c+1) * (2 if f != 0 else 1)
    sq2 = (x2-k) * (y2-y1) * (c+1)
    sq = sq1 + sq2
elif x2 <= k:
    sq = (x2-x1) * (y2-y1) * (c+1) * (2 if f != 0 else 1)
else:
    sq = (x2-x1) * (y2-y1) * (c+1)
print(w * h - sq)