def solution(numbers):
    ans, stack = [], []
    while numbers:
        num = numbers.pop()
        if not stack:   
            ans.append(-1)
            stack.append(num)
        else:
            while stack: 
                if stack[-1] > num: # 뒤 큰 수인 경우
                    ans.append(stack[-1])
                    stack.append(num)
                    break
                stack.pop() # 뒤 큰 수가 나올 때 까지
            else: # 뒤 큰 수를 못찾아서 스택이 비게 됨 (break에 의해 while문이 종료되지 않은 경우)
                ans.append(-1)
                stack.append(num)    
    return ans[::-1]