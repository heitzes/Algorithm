from collections import defaultdict
n = int(input())
nlist = [input() for _ in range(n)]
anslist = []
for word in nlist:
    wdict = defaultdict(int)
    word = word + ' '
    for i in range(len(word)-1):
        wdict[word[i]] += 1
        if wdict[word[i]] == 3:
            if word[i+1] != word[i]:
                anslist.append("FAKE")
                break
            wdict[word[i]] = -1
    else:
        anslist.append("OK")
for ans in anslist:
    print(ans)