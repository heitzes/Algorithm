from itertools import product
def solution(users, emoticons):
    answer = []
    def count(p):
        sign, sell = 0, 0
        for user in users:
            c, money = user
            buy = 0
            for i, v in enumerate(p):
                if v >= c:
                    buy += (emoticons[i] * (100-v)/100)
            if buy >= money:
                sign += 1
                buy = 0
            sell += buy
        answer.append([sign, sell])
            
    
    for percent in product(range(10, 50, 10), repeat=len(emoticons)):
        count(percent)
    answer = sorted(answer, key=lambda x: (-x[0], -x[1]))
    return answer[0]