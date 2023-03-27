from collections import Counter

def solution(X, Y):
    result = []
    X = Counter(X)
    Y = Counter(Y)
    for i in "9876543210":
        if v := min(X.get(i, 0), Y.get(i, 0)):
            result.append(i * v)

    if not result:
        return "-1"
    
    if not any(map(int, result)):
        return "0"
    else:
        return "".join(result)