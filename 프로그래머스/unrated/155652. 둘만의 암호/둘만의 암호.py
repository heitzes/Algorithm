from string import ascii_lowercase
def solution(s, skip, index):
    answer = ''
    chset = set(ascii_lowercase)
    chset -= set(skip)
    chlist = sorted(chset)
    chlen = len(chlist)
    
    for ch in s:
        ind = chlist.index(ch)
        next_ind = ind + index
        answer += (chlist[next_ind%chlen])
    
    return answer