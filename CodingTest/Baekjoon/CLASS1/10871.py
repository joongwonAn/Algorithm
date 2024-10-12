n, x = map(int, input().split())
nList = list(map(int, input().split()))

for i in range(n):
  if(nList[i] < x):
    print(nList[i], end = " ")