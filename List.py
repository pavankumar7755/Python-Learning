"""Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with 
different qualities and usage."""

#list indicates with   "[ ]"  --> square Brackets 

'''spklist=["apple","banana","mango"]
print(spklist)'''

'''List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], 
the second item has index [1] etc.'''


#allow duplicate values
'''spklist=["apple","banana","mango","apple"]
spklist1=[1,2,3,4,5]
spklist2=[True,False]
print(len(spklist))
print(spklist1)
print(spklist2)'''

#list()  constructor

'''spk=(1,2,3,4,5)
thespk=list((spk))
print(thespk)'''


#index always start with 0
'''list=[1,2,3,4]
print(list[1])
print(list[1:3])
'''

'''spk=["cars","bikes","vans","buses"]
if "van" in spk:
  print("yes i have that list")
else:
  print("No!")  '''

#--> important note
#list,tuple,set,dictionary
"""When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, 
and, it could mean an increase in efficiency or security"""