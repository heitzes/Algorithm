from collections import Counter
wlen, slen = map(int, input().split())
word, string = input(), input()
wcnt = Counter(word)
scnt = Counter(string[:wlen])
answer = 0 if wcnt!=scnt else 1
for i in range(slen-wlen):
    scnt[string[i]] -= 1
    scnt[string[i+wlen]] += 1
    for w in word:
        if wcnt[w] != scnt[w]:
            break
    else:
        answer += 1
print(answer)