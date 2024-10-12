num = [int(input()) for _ in range(9)]

# maxNum = num[0]
# maxIndex = 0
# for i in range(9):
#     if maxNum < num[i]:
#         maxNum = num[i]
#         maxIndex = i + 1
#
# print(maxNum)
# print(maxIndex)

print(max(num))
print(num.index(max(num)) + 1)