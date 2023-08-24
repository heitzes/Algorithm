def solution(arr):
    answer = 1
    prime = [[0]*101 for _ in range(len(arr))]
    for i in range(len(arr)):
        num = arr[i]
        for j in range(2, 100):
            if num == 1: break
            while num % j == 0: 
                prime[i][j] += 1
                num /= j
    for k in range(2, 100):
        maxi = 0
        for i in range(len(arr)):
            maxi = max(maxi, prime[i][k])
        answer *= k ** maxi    
    return answer