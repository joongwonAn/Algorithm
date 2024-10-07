table = []
for _ in range(9):
  table.append(list(map(int, input().split())))
  
max_num = 0
max_row, max_col = 0, 0

for i in range(9):
  for j in range(9):
    if (max_num <= table[i][j]):
      max_num = table[i][j]
      max_row = i + 1
      max_col = j + 1

print(max_num)
print(max_row, max_col, end = ' ')
      