from itertools import combinations

# 입력
n, m = map(int, input().split())
nList = list(map(int, input().split()))

mList = []
for card in combinations(nList, 3):
    if sum(card) <= m:
        mList.append(sum(card))

print(max(mList))