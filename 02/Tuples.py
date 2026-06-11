>>> tea_types = ("Black", "Green", "oolong")
>>> tea_types
('Black', 'Green', 'oolong')

# accessing elements same as lists slicing dicing n all
>>> tea_types[0]
'Black'
>>> tea_types[1]
'Green'

# since tuples are immutable hence assigned values cant be changed
>>> tea_types[0] = "Lemon"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    tea_types[0] = "Lemon"
    ~~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment


>>> len(tea_types)
3
>>> more_tea = ("Herbal", "Earl Grey")
>>> all_tea = more_tea + tea_types
>>> all_tea
('Herbal', 'Earl Grey', 'Black', 'Green', 'oolong')
>>>
>>> if "Green" in all_tea:    
...     print("I have green tea")
... 
I have green tea

>>> more_tea = ("Herbal", "Earl Grey", "Herbal") 
>>> more_tea
('Herbal', 'Earl Grey', 'Herbal')
>>> more_tea.count("Herbal")
2
#for items that are not present will simply return 0
>>> more_tea.count("adrak") 
0


>>> tea_types=("Masala", "Green", "Oolong") 
>>> tea_types
('Masala', 'Green', 'Oolong')
>>> (black, green, oolong) = tea_types
>>> 
>>> black
'Masala'
>>> green 
'Green'
>>> oolong
'Oolong'

#to check for teh type of a variable 
>>> type(tea_types)
<class 'tuple'>