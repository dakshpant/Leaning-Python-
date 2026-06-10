>>> chai_types = {"Masala":"spicy", "Ginger":"Zesty","Green":"Mild"}
>>> chai_types
{'Masala': 'spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
>>> chai_types[1]
Traceback (most recent call last):
  File "<python-input-7>", line 1, in <module>
    chai_types[1]
    ~~~~~~~~~~^^^
KeyError: 1
>>> chai_types["Masala"]
'spicy'
>>> chai_types.get("Ginger")
'Zesty'
>>> chai_types.get("oolong")
>>> chai_types["Green"] = "Fresh"
>>> chai_types
{'Masala': 'spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
>>> 

>>> for chai in chai_types:
...     print(chai)
...     
Masala
Ginger
Green


...     print(chai, chai_types[chai])
...     
Masala spicy
Ginger Zesty
Green Fresh

>>> for key, value in chai_types.items():
...     print(key, value)                                                                                                                       
...     
Masala spicy
Ginger Zesty
Green Fresh

 print(len(chai_types))
3


chai_type["Earl Grey"] = "Citrus"

>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}

#Teh delete del remove the item from the memory unlike pop() which returns teh deleted item
>>> del chai_types["Green"]
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Earl Grey': 'Citrus'}

