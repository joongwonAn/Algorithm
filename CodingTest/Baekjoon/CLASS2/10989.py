# try1) sort() 사용 - 메모리 초과
# n = int(input())
# numList = [int(input()) for _ in range(n)]
# numList.sort()
#
# print(numList)

# try2) 계수 정렬 사용 - 시간 초과
# n = int(input())
# arr = [0] * 10001
#
# for _ in range(n):
#     num = int(input())
#     arr[num] += 1
#
# for i in range(10001):
#     if arr[i] != 0:
#         for j in range(arr[i]):
#             print(i)


# try3) sys 라이브러리 사용
import sys

n = int(sys.stdin.readline())
arr = [0] * 10001

for _ in range(n):
    num = int(sys.stdin.readline())
    arr[num] += 1

for i in range(10001):
    if arr[i] != 0:
     for _ in range(arr[i]):
         print(i)
