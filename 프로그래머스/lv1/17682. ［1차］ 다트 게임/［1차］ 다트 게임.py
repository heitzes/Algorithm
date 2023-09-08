import re
def solution(dartResult):
    index = []
    strs = re.findall(r'[0-9]+[SDT][*#]?', dartResult)
    point, option = [0, 0, 0], [0, 0, 0]
    d = {'S': 1, 'D': 2, 'T': 3}
    for idx, string in enumerate(strs):
        if string[-1] not in ['*', '#']:
            point[idx] += int(string[:-1]) ** d[string[-1]]
        else:
            point[idx] += int(string[:-2]) ** d[string[-2]]
            if string[-1] == '*': 
                option[idx] += 1
                if idx != 0: option[idx-1] += 1
            else: point[idx] *= -1 
    answer = sum([point[i]*(2**option[i]) for i in range(3)])
    return answer