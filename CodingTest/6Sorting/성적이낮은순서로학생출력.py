n = int(input())

array = []
for i in range(n):
  input_data = input().split()
  array.append((input_data[0], int(input_data[1])))

#key를 이용하여, 점수를 기준으로 정렬
array = sorted(array, key = lambda student: student[1])

for student in array:
  print(student[0], end=' ')