number = list(map(int, input().split()))

total = 0
for i in range(len(number)):
    total += number[i] * number[i]

print(total % 10)
