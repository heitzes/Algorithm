def solution(s, skip, index):
    answer = ''
    skiplist = [i for i in skip]
    for ch in s:
        i = 0
        while i < index:
            next_ord = ord(ch) + 1 
            if next_ord > 122:
                next_ord -= 26                
            next_ch = chr(next_ord)
            if next_ch not in skiplist:
                i += 1
            ch = next_ch
        answer += ch
        
    return answer