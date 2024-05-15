#현재 나이트 위치 입력받기
input_data = input()
r = int(input_data[1])
c = int(ord(input_data[0])) - int(ord('a')) + 1

#나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2),
         (-2, 1)]

#8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
count = 0
for step in steps:
  #이동하고자 하는 위치 확인
  next_r = r + step[0]
  next_c = c + step[1]
  #해당 위치로 이동이 가능하다면 카운트 증가
  if next_r >= 1 and next_r <= 8 and next_c >= 1 and next_c <= 8:
    count += 1

print(count)
