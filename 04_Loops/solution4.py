# m1
inputStr = "Python"

reversedStr = ""

for char in inputStr:
    reversedStr = char + reversedStr

print(reversedStr)


# m2
# Using start stop and step  
inputStr2 = "Python"

for i in range(len(inputStr2) - 1, -1, -1):
    print(inputStr2[i], end="")


# input_str = "Python"

# left = 0
# right = input_str.__sizeof__

# while(left < right):
#     input_str[left], input_str[right] = input_str[right], input_str[left]
#     left += 1
#     right += 1

# print(''.join(input_str))