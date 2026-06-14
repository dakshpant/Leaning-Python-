 tea_variety = ["Black", "Mas\
ala", "White"]
>>> tea_variety_copy = tea_varie\
ty
>>> print(tea_variety_copy)
['Black', 'Masala', 'White']
>>> 
>>> 
>>> tea_variety_copy = tea_varie\
ty.copy()


# using copy method creates a new space in the menory and the tea_variety_copy points to that 

#  but in teh case of tea_variety_copy = tea_variety both the variables point to the same space in memory and any change in one will reflect in the other 
# in this case if we change the value of tea_variety then  the value of tea_variety will also change
# but in the case of tea_variety_copy = tea_variety.copy() both the variables point to different space in memory and any change in one will not reflect in the other hench chanhe in one will not affect the other


 range(10)
range(0, 10)
>>> print(range(10))
range(0, 10)
>>> 
>>> squared_num  = [x**2 for x i\
n range(10)]

>>> squared_num
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]