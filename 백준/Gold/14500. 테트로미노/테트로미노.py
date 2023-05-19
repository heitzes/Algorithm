N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
one_four = [[1, 1, 1, 1]]
four_one = [[1], [1], [1], [1]]
two_two = [[1, 1], [1, 1]]
two_three = [[[1,1,1], [1,0,0]], [[0,0,1],[1,1,1]], 
[[1,0,0],[1,1,1]], [[1,1,1], [0,0,1]], [[0,1,1],[1,1,0]], 
[[1,1,0],[0,1,1]], [[0,1,0],[1,1,1]], [[1,1,1], [0,1,0]]]
three_two = [list(map(list, zip(*i))) for i in two_three]

def make_board(arr, a, b):
    board = []
    for i in range(a, a+len(arr)):
        board.append(maps[i][b:b+len(arr[0])])
    return board

def equal(arr1, arr2):
    cnt = 0
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            if arr2[i][j] == 1:
                cnt += arr1[i][j]
    return cnt
all_array = []
all_array.append(one_four)
all_array.append(four_one)
all_array.append(two_two)
all_array.extend(two_three)
all_array.extend(three_two)
maxi = 0
for arr in all_array:
    for i in range(N-len(arr)+1):
        for j in range(M-len(arr[0])+1):
            cut = make_board(arr, i, j)
            maxi = max(equal(cut, arr), maxi)
print(maxi)