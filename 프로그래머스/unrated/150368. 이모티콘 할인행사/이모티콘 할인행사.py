from itertools import product
import heapq
def solution(users, emoticons):
    answer = set()
    ems = len(emoticons)
    percents = list(map(list, product(range(10,50,10), repeat = ems)))
    for percent in percents: # 할인 정책 마다
        buyer, earn = 0, 0
        for user in users: # 유저가 구매할 임티
            up, money = user # 유저의 할인 기준, 예산
            buy = 0
            for i in range(ems):
                if percent[i] >= up:
                    buy += int((emoticons[i] * (100-percent[i])) / 100)
                if buy >= money:
                    buyer += 1
                    break
            else:
                earn += buy
        answer.add((buyer, earn))
    return (list(max(answer)))