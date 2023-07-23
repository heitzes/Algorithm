n = int(input())
nlist = input().split()
cset = set()
for i in range(n):
    topping = nlist[i]
    if topping[-6:] == "Cheese":
        cset.add(topping)
if len(cset) >= 4:
    print("yummy")
else:
    print("sad")