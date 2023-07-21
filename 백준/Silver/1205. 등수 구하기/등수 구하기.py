from collections import deque
n, taesu, p = map(int, input().split())
def solution():
    global n, taesu, p
    if not n:
        return 1
    else:
        ans = 1
        nlist = list(map(int, input().split()))
        nlist = deque(sorted(nlist, reverse=True))
        if len(nlist) == p: # 다 참
            if nlist[-1] >= taesu: # 못 들어감
                return -1
            else: # 들어갈 수 있음
                while nlist:
                    if taesu >= nlist[0]: # 태수가 크거나 같은 경우
                        return ans
                    else: # 태수가 작은 경우
                        ans += 1
                        nlist.popleft()
                return ans
        else: # 다 안참
            while nlist:
                if taesu >= nlist[0]: # 태수가 크거나 같은 경우
                    return ans
                else: # 태수가 작은 경우
                    ans += 1
                    nlist.popleft()
            return ans
print(solution())