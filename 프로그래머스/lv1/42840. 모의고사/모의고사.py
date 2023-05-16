def solution(answers):
    answer = []
    n = len(answers)
    supo_1 = ([1,2,3,4,5] * ((n // 5)+1))[:n] 
    supo_2 = ([2,1,2,3,2,4,2,5] * ((n // 8)+1))[:n]
    supo_3 = ([3,3,1,1,2,2,4,4,5,5,] * ((n // 10)+1))[:n]
    s1, s2, s3 = 0, 0, 0
    for i in range(n):
        if supo_1[i] == answers[i]:
            s1 += 1
        if supo_2[i] == answers[i]:
            s2 += 1
        if supo_3[i] == answers[i]:
            s3 += 1
    scores = [s1, s2, s3]
    maxi = max(scores)
    for i in range(1, 4):
        if scores[i-1] == maxi:
            answer.append(i)
    return answer