###선택정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
  min_index = i  #가장 작은 원소의 인덱스
  for j in range(i + 1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i]  #스와프

print(array)

###삽입정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
  for j in range(i, 0, -1):
    if array[j] < array[j - 1]:
      array[j], array[j - 1] = array[j - 1], array[j]
    else:
      break

print(array)

###퀵 정렬 (전통적)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
  if start >= end:  #원소가 1개일 경우 종료
    return
  pivot = start  #피벗은 첫 번째 원소
  left = start + 1
  right = end
  while left <= right:
    #피벗보다 큰 데이터를 찾을 때까지 반복
    while left <= end and array[left] <= array[pivot]:
      left += 1
    #피벗보다 작은 데이터를 찾을 때까지 반복
    while right > start and array[right] >= array[pivot]:
      right -= 1
    if left > right:  #엇갈렸다면 작은 데이터와 피벗을 교체
      array[right], array[pivot] = array[pivot], array[right]
    else:  #안 엇갈렸아면 작은 데이터와 큰 데이터를 교체
      array[left], array[pivot] = array[pivot], array[left]
    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
  quick_sort(array, start, right - 1)
  quick_sort(array, right + 1, end)

  quick_sort(array, 0, len(array) - 1)
  print(array)


###퀵 정렬(py ver)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
  #리스트가 하나 이하의 원소만 담고 있다면 종료
  if len(array) <= 1:
    return array

  pivot = array[0]  #피벗은 첫 번째 원소
  tail = array[1:]  # 피벗을 제와한 리스트

  left_side = [x for x in tail if x <= pivot]  #분할된 왼쪽 부분
  right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽 부분
  #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
  return quick_sort(left_side) + quick_sort(right_side)


print(quick_sort(array))

###계수 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
#모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
  count[array[i]] += 1  #각 데이터에 해당하는 인덱스 값 증가

for i in range(len(count)):  #리스트에 기록된 정렬 정보 확인
  for j in range(count[i]):
    print(i, end=' ')  #띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력

### 파이썬의 정렬 라이브러리
##soreted()
#반환되는 결과는 리스트 자료형
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print(result)

###sort()
#별도의 정렬된 리스트 반환 X, 내부원소가 바로 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sort(array)
print(result)

###key활용 정렬
array = [('바나나', 2), ('사과', 5), ('당근', 3)]


def setting(data):
  return data[1]


result = sorted(array, key=setting)
print(result)

###
#문제에서 별도의 요구가 없다면 단순히 정렬해야 하는 상황에서는 기본 정렬 라이브러리 사용
#데이터의 범위가 한정되어 있으며 더 빠르게 동작해야 할 때는 계수 정렬 사용
