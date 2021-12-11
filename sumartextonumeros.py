nums = input("Introduzca los números seguidos. ")

nums_sum = 0

for i in range(len(nums)):
    nums_sum += int(nums[i])

print(nums_sum)
