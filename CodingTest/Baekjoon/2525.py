A, B = map(int, input().split())
C = int(input())

time = A * 60 + B + C
A = time // 60
B = time % 60

if (A > 23):
  A = A -24

if (B>60):
  B = B - 60
  
print(A, B)