from collections import deque
import re

def solution(new_id: str):
    # 1
    new_id = new_id.lower()

    # 2
    new_id = re.sub("[^0-9|a-z|A-Z|\-|_|.]", "", new_id)

    # 3
    d = deque([])
    for c in new_id:
        if d and d[-1] == "." and c == ".":
            continue
        d.append(c)

    # 4
    if d and d[0] == ".":
        d.popleft()
    if d and d[-1] == ".":
        d.pop()
    
    # 5
    if not d:
        d.append("a")
    
    # 6
    if len(d) >= 16:
        d = list(d)[:15]
    if d[-1] == ".":
        d.pop()
    
    # 7
    while len(d) <= 2:
        d.append(d[-1])
    
    return "".join(d)