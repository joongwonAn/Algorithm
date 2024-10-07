table = []
for _ in range(5):
  table.append(list(map(int, input().split())))

# for i in range(5):
#   if(len(table[i]) < 16):
#     for _ in range(15 - len(table[i])):
#       table[i].append(None)

for i in range(15):
  for j in range(5):
    if (table[j][i] is not None):
      print(table[j][i], end = "")