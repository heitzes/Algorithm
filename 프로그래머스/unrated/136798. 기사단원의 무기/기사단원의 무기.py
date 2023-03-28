def solution(number, limit, power):
    answer = 0
    arr = [0, 1]
    for n in range(2, number+1):
        cnt = 2
        for i in range(2, int(n ** (1/2) + 1)):
            if n % i:
                continue
            if n == i * i:    
                cnt += 1
            else:
                cnt += 2
        arr.append(cnt)
    return sum([n if n <= limit else power for n in arr])

print(solution(5, 3, 2))
