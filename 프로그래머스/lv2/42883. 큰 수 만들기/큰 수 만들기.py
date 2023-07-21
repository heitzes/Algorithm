def solution(number, k):
    stack = []
    for n in number:
        while stack and k > 0 and int(n) > int(stack[-1]):
            stack.pop()
            k -= 1
        stack.append(n)
    return ''.join(stack if k==0 else stack[:-k])