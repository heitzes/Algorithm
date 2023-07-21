n, m = map(int, input().split())
nlist = sorted(input().split())
aeiou = set(['a', 'e', 'i', 'o', 'u'])
moeum, jaeum = [0]*(26), [0]*(26)
password = set()
def dfs(ind, s):
    if len(s) >= n:
        if not (sum(moeum) < 1 or sum(jaeum) < 2): 
            password.add(s)
        s = s[:-1]
        return
    for i in range(ind+1, m-(n-len(s))+1):
        if nlist[i] in aeiou:
            moeum[ord(nlist[i])-97] = 1
        else:
            jaeum[ord(nlist[i])-97] = 1
        dfs(i, s+nlist[i])
        if nlist[i] in aeiou:
            moeum[ord(nlist[i])-97] = 0
        else:
            jaeum[ord(nlist[i])-97] = 0
dfs(-1, '')
for i in sorted(password):
    print(i)