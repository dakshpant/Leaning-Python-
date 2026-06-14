numb = 5

fact = 1

print("The factorial of ", numb , "is:", end=" ")

while(numb>0):
    fact *= numb
    numb -= 1
print(fact)
