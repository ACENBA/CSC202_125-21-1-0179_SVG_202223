#Creating Lists using List Comprehension
#For Loop
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

#List Comprehension
new_list = [n + 1 for n in numbers]

#String as list
name = "Angela"
letters_list = [letter for letter in name]

#Range as List
range_list = [num * 2 for num in range(1,5)]

#Conditional List Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

#List Case Conversion
short_names = [name for name in names if len(name) < 5]

#List Case Conversion
long_names = [name.upper() for name in names if len(name) > 5]