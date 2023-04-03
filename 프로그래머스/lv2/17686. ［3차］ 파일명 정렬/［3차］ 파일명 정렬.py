def solution(files):
    """
    파일명 하나하나 HEAD, NUMBER, TAIL을 나눈다.
    NUMBER의 시작: 처음으로 숫자가 나오는 곳
    NUMBER의 끝: 처음으로 문자가 나오는 곳의 전
    이 때, NUMBER의 끝이 파일명의 끝과 일치하는 edge case에 주의 
    
    세 부분으로 나눈 후, 정렬을 위해 각 파일을 [HEAD, NUMBER, index] 형태로 다시 저장
    """
    answer, new_files = [], []
    for ind, file in enumerate(files):
        flen = len(file)
        start, end = 0, flen
        for i in range(flen):
            if not start and file[i].isdigit():
                start = i
            if start and not file[i].isdigit():
                end = i
                break
        new_files.append([file[:start].lower(), file[start:end], ind])
    new_files = sorted(new_files, key = lambda x: (x[0], int(x[1]), x[2]))
    answer = [files[f[-1]] for f in new_files]
    return answer