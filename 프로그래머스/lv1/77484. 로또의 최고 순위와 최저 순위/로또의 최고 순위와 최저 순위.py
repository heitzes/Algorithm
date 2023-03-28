def solution(lottos: list, win_nums: list):
    table = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5}
    base = len(set(win_nums) & set(lottos))
    return [table.get(base + lottos.count(0), 6), table.get(base, 6)]