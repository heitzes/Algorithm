def solution(numbers):
    count = 0
    check = set()
    visited = [0] * (len(numbers))
    
    def power_set(string):
        masks = [1 << i for i in range(len(string))]
        for i in range(1, 1 << len(string)):
            yield [n for n, mask in zip(string, masks) if mask & i]
    
    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, int(n ** (1 / 2)) + 1):
            if n % i == 0:
                return False
        return True
    
    def dfs(s, n, S):
        if len(s) == n:
            num = int(s)
            if num not in check and is_prime(num):
                nonlocal count
                count += 1
            check.add(num)
        
        for i in range(n):
            if not visited[i]:
                visited[i] = 1
                dfs(s+S[i], n, S)
                visited[i] = 0
    
    for S in power_set(numbers):
        dfs("", len(S), S)
    
    return count