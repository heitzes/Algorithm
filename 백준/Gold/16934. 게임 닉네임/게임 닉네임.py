from collections import defaultdict
n = int(input())
alias = set()
users = defaultdict(int)
for _ in range(n):
    nick = input()
    if nick in alias:
        if users[nick] == 0:
            print(nick)
        else:
            print(nick + str(users[nick]+1))
        users[nick] += 1
        continue
    find = False
    for i in range(1, len(nick)+1):
        use = nick[:i]
        if use not in alias and not find:
            print(use)
            find = True
        alias.add(use)
    users[nick] += 1