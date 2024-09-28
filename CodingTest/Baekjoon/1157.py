words = input().upper()
wordsList = list(set(words))

cnt = []
for i in wordsList:
  cnt.append(words.count(i))

if ( cnt.count((max(cnt))) > 1):
  print("?")
else:
  print(wordsList[ cnt.index(max(cnt)) ])