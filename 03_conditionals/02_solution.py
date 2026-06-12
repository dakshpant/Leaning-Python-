# age = int(input("Enter Your Age:"))
# day = str(input("What day it is:")).capitalize

# if age < 18 and day == "Wednesday":
#     print("Enjoy movie at $6")
# elif age > 18 and day == "Wednesday":
#     print("Enjoy movie at $10")
# elif age < 18 and day != "Wednesday":
#     print("Enjoy movie at $8")
# else:
#     print("Enjoy movie at $12")


age = int(input("enter your age:"))
day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price -= 2

print("Your movie ticket costs $", price)    
