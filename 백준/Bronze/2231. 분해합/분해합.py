n = int(input())
def make_sum(k):
    return k + sum(list(map(int, list(str(k)))))
for i in range(1, n):
    if n == make_sum(i):
        print(i)
        break
else:
    print(0)