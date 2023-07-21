n = int(input())
isPrime = [True] * (n+1)
isPrime[0], isPrime[1] = False, False
prime = []
for i in range(2, n+1):
    if not isPrime[i]: continue
    prime.append(i)
    for j in range(i*2, n+1, i):
        isPrime[j] = False
cnt, s, e = 0, 0, 0
answer = 0
while True:
    if cnt >= n:
        cnt -= prime[s]
        s += 1
    elif e == len(prime):
        break
    else:
        cnt += prime[e]
        e += 1 
    if cnt == n: answer += 1
print(answer)