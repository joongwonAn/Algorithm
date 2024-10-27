# 입력
len = int(input())
userList = input()

M = 1234567891
R = 31

# ord('a') = 97 이용하여 알파벳에 고유한 계수 부여 (1~26)
hashResult = 0
for i in range(len):
    num = ord(userList[i]) - 96
    hashResult += num * (R ** i)


print(hashResult % M)