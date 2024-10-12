# words = []
# for _ in range(5):
#   a = input()
#   words.append(a)

# 리스트 컴프리헨션(list comprehension): 리스트를 만드는 간결한 방법 제공
words = [input() for _ in range(5)]

for j in range(15):
  for i in range(5):
    if (j < len(words[i])):
      print(words[i][j], end ='')
