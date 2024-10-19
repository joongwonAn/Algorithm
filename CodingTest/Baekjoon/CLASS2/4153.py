while True:
    nums = list(map(int, input().split()))

    if sum(nums) == 0:
        break

    maxNum = max(nums)
    nums.remove(maxNum)

    if nums[0]**2 + nums[1]**2 == maxNum**2:
        print("right")
    else:
        print("wrong")
