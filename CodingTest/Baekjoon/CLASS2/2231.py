n = int(input())

mList = []
for m in range(1, n):
    if n == (m + sum(map(int, str(m)))):
        mList.append(m)

if not mList:
    print("0")
else:
    print(min(mList))