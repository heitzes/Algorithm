from collections import defaultdict
auth = {'7': 'RWX', '6': 'RW', '5': 'RX', '4':'R', '3': 'XWR', '2': 'WR', '1': 'X', '0': ''}
u, f = map(int, input().split())
groups = defaultdict(set)
files = defaultdict(list)
for i in range(u):
    info = input().split()
    groups[info[0]].add(info[0])
    if len(info) > 1:
        for g in info[1].split(','):
            groups[g].add(info[0])
for j in range(f):
    finfo = input().split()
    files[finfo[0]] = finfo[1:]
q = int(input())
questions = [input().split() for _ in range(q)]
for question in questions:
    user, file, access = question
    num, owner, gp = files[file]
    if user == owner:
        user_auth = set(auth[num[0]]) | set(auth[num[1]]) | set(auth[num[2]])
    elif gp in groups and user in groups[gp]:
        user_auth = set(auth[num[1]]) | set(auth[num[2]])
    else:
        user_auth = set(auth[num[2]])
    if set(access).issubset(user_auth):
        print(1)
    else:
        print(0)