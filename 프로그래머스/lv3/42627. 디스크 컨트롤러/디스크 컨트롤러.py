from collections import deque
def solution(jobs):
    njobs = len(jobs)
    answer, time = 0, 0
    while jobs:
        wait = sorted([[i, n] for i, n in jobs if i<=time], key=lambda x: x[-1])
        if not wait:
            time += 1
            continue
        task = wait[0]
        time += task[1]
        jobs.remove(task)
        answer += (time - task[0])
    return answer // njobs