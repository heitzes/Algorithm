from collections import defaultdict
import bisect

n, q = map(int, input().split())
logs = defaultdict(list)
queries = []

def date_to_second(date):
    y, m, d = map(int, date)
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = [0]
    years = [2000, 2004, 2008, 2012, 2016, 2020]
    if y in years:
        month[1] = 29
    plus = bisect.bisect_left(years, y)
    for i in range(12):
        days.append(days[-1] + month[i])
    return ((y-2000) * 365 + plus + (days[m-1] + d-1)) * 86400

def time_to_second(time):
    h, m, s = map(int, time)
    return 3600*h + 60*m + s

for i in range(n):
    log = input().split()
    sec1 = date_to_second(log[0].split('-'))
    time, level = log[1].split('#')
    sec2 = time_to_second(time.split(':'))
    logs[int(level)].append(sec1 + sec2)

for j in range(q):
    start, end, level = input().split('#')
    s_date, s_time = start.split()
    s_sec1 = date_to_second(s_date.split('-'))
    s_sec2 = time_to_second(s_time.split(':'))

    e_date, e_time = end.split()
    e_sec1 = date_to_second(e_date.split('-'))
    e_sec2 = time_to_second(e_time.split(':'))

    queries.append([int(level), s_sec1+s_sec2, e_sec1+e_sec2])

for query in queries:
    count = 0
    for lev in range(query[0], 7):
        lower = bisect.bisect_left(logs[lev], query[1])
        upper = bisect.bisect_right(logs[lev], query[2])
        count += (upper - lower)
    print(count)