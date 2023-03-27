from collections import Counter

def solution(X, Y):
    result = []
    X = Counter(X)
    Y = Counter(Y)
    for i in "9876543210":
        if v := min(X.get(i, 0), Y.get(i, 0)):
            for _ in range(v):
                result.append(i)

    if not result:
        return "-1"
    if result[0] == "0" and result[-1] == "0":
        return "0"
    return "".join(result)