def solution(number, k):
    stack = []
    for n in number:
        while stack and k > 0:
            if int(n) <= int(stack[-1]):
                break
            stack.pop()
            k -= 1
        stack.append(n)
    while stack and k > 0:
        stack.pop()
        k -= 1
    return ''.join(stack)