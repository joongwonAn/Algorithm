n = int(input())
nList = list(map(int, input().split()))

maxNum = nList[0]
minNum = nList[0]
for i in nList:
    if maxNum < i:
        maxNum = i
    if minNum > i:
        minNum = i

print(minNum, maxNum)