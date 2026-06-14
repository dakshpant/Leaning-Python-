numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
count = 0
for nums in numbers:
    if nums > 0:
        count += 1
        print(nums)

print("Total positive numbers:", count)