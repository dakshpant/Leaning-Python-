>>> chai  = "Lemon Chai"
>>> chai
'Lemon Chai'
>>> print(chai)
Lemon Chai

>>> first_char = chai[0]
>>> print(first_char)
L

>>> chai
'Lemon Chai'
>>> 
>>> slice_chai = chai[0:6]
>>> print(slice_chai)
Lemon

# Converting string to list 
>>> chai = "lemon, ginger, masal , mint"
>>> print(chai.split())
['lemon,', 'ginger,', 'masal,', 'mint']
>>> print(chai.split(", "))
['lemon', 'ginger', 'masal', 'mint']


>>> chai = "Masala Chai"
>>> print(chai.find("Chai"))
7
>>> print(chai.find("chhai"))
-1

>>> chai  = "Masala Chai Chai ch\
ai"
>>> print(chai.count("Chai"))
2


>>> chai_type = "Masala"
>>> qualtity = 2
>>> order = "i ordered {} cups o\
f chai"
>>> 
>>> print(order.format(qualtity, chai_type))
i ordered 2 cups of chai

>>> chai_variety = ["lemon", "ma\
sala", "Ginger"]
>>> 
>>> chai_variety
['lemon', 'masala', 'Ginger']
>>> print("".join(chai_variety))
lemonmasalaGinger

>>> print(" ".join(chai_variety)\
)
lemon masala Ginger
>>> print("-".join(chai_variety)\
)
lemon-masala-Ginger
>>> print(", ".join(chai_variety\
))
lemon, masala, Ginger

>>> chai = "masala chai"
>>> 
>>> print(len(chai))
11
>>> 
>>> chai
'masala chai'
>>> for letter in chai:
...     print(letter)1 
...
m
a
s
a
l
a
 
c
h
a
i

>>> chai = "He said, \"Masala Ch\
ai si awesome\" " # using double quotes and \ for using t doubel quotes in string
>>> chai
'He said, "Masala Chai si awesome" '


chai = "masala\nchai"
>>> chai
'masala\nchai'
>>> print(chai)
masala
chai

# r means raw string and it will ignore the escape sequence
 chai  = r"c:\user\pwd\"
  File "<python-input-102>", line 1
    chai  = r"c:\user\pwd\" 
            ^
SyntaxError: unterminated string literal (detected at line 1); perhaps you escaped the end quote?
>>> chai = r"c:\\user\\pwd\\"
>>> print(chai)
c:\\user\\pwd\\
>>> 
>>> chai  = r"c:\user\pwd"
>>> print(chai)
c:\user\pwd
>>> 