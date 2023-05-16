def solution(routes):
    answer = 1
    routes = sorted([sorted(route) for route in routes],reverse=True)
    cur = routes.pop()
    while routes:
        car = routes.pop()
        if car[0] > cur[-1]:
            answer += 1
            cur = car
        else:
            cur = [max(cur[0], car[0]), min(cur[1], car[1])]
    return answer