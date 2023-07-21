from collections import deque
answer = tuple([1, 2, 3, 4, 5, 6, 7, 8, 0])
initial = []
check = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5], 3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8], 6: [3, 7], 7: [4, 6, 8], 8: [5, 7]}
for _ in range(3):
    initial.extend(list(map(int, input().split())))
dq, vi = deque([[initial, 0]]), set([tuple(initial)])
def solution():
    while dq:
        arr, cnt = dq.popleft()
        if tuple(arr) == answer:
            return cnt
        ind = arr.index(0)
        for ch in check[ind]:
            arr[ch], arr[ind] = arr[ind], arr[ch]
            if tuple(arr) not in vi:
                vi.add(tuple(arr))
                dq.append([arr[:], cnt+1])
            arr[ch], arr[ind] = arr[ind], arr[ch]
    return -1
print(solution())