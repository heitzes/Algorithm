def change(t):
    h, m = int(t[0]), int(t[1])
    return h*60 + m
def solution(book_time):
    answer = 1
    book_time = sorted([[change(time[0].split(":")), change(time[1].split(":"))] for time in book_time])
    current = [book_time.pop(0)[1]+10]
    while book_time:
        new = book_time.pop(0)
        for i, c in enumerate(current):
            if c <= new[0]:
                current[i] = new[1] + 10
                break
        else:
            answer += 1
            current.append(new[1] + 10)
        current.sort()
    return answer