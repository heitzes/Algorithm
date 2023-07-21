from collections import deque
def new_deque(arr, qr):
    dq = deque([])
    x1, y1, x2, y2 = qr
    dq.extend(arr[x1-1][y1-1:y2])
    dq.extend([arr[i][y2-1] for i in range(x1, x2-1)])
    dq.extend(arr[x2-1][y1-1:y2][::-1])
    dq.extend([arr[i][y1-1] for i in range(x1, x2-1)][::-1])
    dq.rotate()
    return dq
def change(arr, qr, deq):
    x1, y1, x2, y2 = qr
    for i in range(y2-y1+1):
        arr[x1-1][y1-1+i] = deq[i]
        arr[x2-1][y2-1-i] = deq[x2-x1+y2-y1+i]
    for j in range(x2-x1-1):
        arr[x1+j][y2-1] = deq[y2-y1+1+j]
        arr[x2-2-j][y1-1] = deq[x2-x1+y2-y1+y2-y1+1+j]
    return arr
def solution(rows, columns, queries):
    """
    8, 9, 10, 16, ... 14
    14, 8, 9, 10, ... 20
    이렇게 돌린 다음에 갈아 끼우는 방식으로 구현해보자
    """
    result = []
    array = [[i*columns + (j+1) for j in range(columns)] for i in range(rows)]
    for query in queries:
        dq = new_deque(array, query)
        array = change(array, query, dq)
        result.append(min(dq))
    return result