# 입력받기
n = int(input())
scores = list(map(int, input().split()))

M = int(max(scores))
newScores = []
for score in scores:
    newScores.append(score / M * 100)

print(sum(newScores) / n)

