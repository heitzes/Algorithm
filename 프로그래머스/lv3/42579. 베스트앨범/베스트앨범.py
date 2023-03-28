def solution(genres, plays):
    genre_table = {}
    zipped = list(zip(range(len(genres)), genres, plays))
    for _, g, p in zipped:
        genre_table[g] = genre_table.get(g, 0) + p

    result = []
    cnt, prev = 0, None
    for i, g, p in sorted(zipped, key=lambda x: (-genre_table[x[1]], -x[2])):
        cnt = cnt + 1 if g == prev else 0
        if cnt >= 2:
            continue
        result.append(i)
        prev = g
    return result