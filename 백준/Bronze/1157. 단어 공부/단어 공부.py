from collections import defaultdict
string = input().lower()
arr = [0] * 26
for i in range(26):
    arr[i] = string.count(chr(97+i))
maxi = max(arr)
if arr.count(maxi) != 1:
    print("?")
else:
    print(chr(arr.index(maxi) + 97).upper())