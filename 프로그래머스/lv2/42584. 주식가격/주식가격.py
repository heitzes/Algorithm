def solution(prices):
    answer = [0]
    stack = [[prices[-1], 0]]
    for price in prices[::-1][1:]:
        cnt = 1
        while stack:
            if price <= stack[-1][0]:
                _, c = stack.pop()
                cnt += c
                continue
            break
        stack.append([price, cnt])
        answer.append(cnt)
    return answer[::-1]