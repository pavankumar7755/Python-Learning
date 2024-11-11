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

#change list iteam

'''spk=["apple","banana","coconut"]
spk[2]="lemon"
print(spk)'''


'''my = ["cars","bikes","vans","helicopter"]
my[1:2]=["scooter","lorry","bicycle"]
print(my)'''

#insert items

'''my = ["cars","bikes","vans","helicopter"]
my.insert(2,"bicycle")
print(my)'''

#append the items

'''my = ["cars","bikes","vans","helicopter"]
my.append("lorry")
print(my)'''

#extend item to list
'''
my = ["cars","bikes","vans","helicopter"]
vehicle=["lorry","bicycle"]
my.extend(vehicle)
print(my)

my = ["cars","bikes","vans","helicopter"]
veh=("scooter","ship")
my.extend(veh)
print(my)'''


#REMOVE LIST
'''
my = ["cars","bikes","vans","helicopter"]
my.remove("cars")
print(my)
#duplicate values
my = ["cars","bikes","vans","cars","helicopter"]
my.remove("cars")
print(my)
'''
#pop 

'''my = ["cars","bikes","vans","cars","helicopter"]
print(len(my))
my.pop(3)
print(len(my))

#pop -->If you do not specify the index, 
# the pop() method removes the last item
my = ["cars","bikes","vans","cars","helicopter"]
my.pop()
print(my)'''

#DEL

'''my = ["cars","bikes","vans","cars","helicopter"]
del my[0]
print(my)'''

'''my = ["cars","bikes","vans","cars","helicopter"]
del my'''

#clear 

'''my = ["cars","bikes","vans","cars","helicopter"]
my.clear()
print(my)'''

#loop through a list
#for loop

'''my = ["cars","bikes","vans","cars","helicopter"]
for i in my:
    print(my)'''
'''
my = ["cars","bikes","vans","cars","helicopter"]
for i in range(len(my)):
    print(my[i])'''

'''my = ["cars","bikes","vans","cars","helicopter"]
for i in my:
    print(i)'''


#while loop

'''my = ["cars","bikes","vans","cars","helicopter"]
i=3
while i<len(my):
  print(my[i])
  i=i+1'''



"""for x in ["cars","lorry","bikes"]:
   print(x)"""

#filter with words
'''my = ["cars","bikes","vans","cars","helicopter"]
#new=[x for x in my if x!="cars"]   -->not equal operator
#new=[x for x in my if "i" in x]
#new=[x for x in my if x=="cars"] 

print(new)'''

'''new=[x for x in range(10)]
print(new)'''

"""new=[x for x in range(10) if x<5]
print(new)
"""
'''my = ["cars","bikes","vans","cars","helicopter"]
new=[x.upper() for x in my]
print(new)'''

'''my = ["cars","bikes","vans","cars","helicopter"]
new=["hello" for x in my]
print(new)'''

'''my = ["cars","bikes","vans","cars","helicopter","lorry","bicycle"]
new=[x if x!="cars" else "---" for x in my]
print(new)'''

#sort
'''my = ["cars","bikes","vans","cars","helicopter"]
my.sort()
print(my)'''
#sort - desscending
'''my = [2,5,3,9,11,34,23,1]
my.sort(reverse=True)
print(my)'''

#reverse
'''my = ["cars","bikes","vans","cars","helicopter"]
my.reverse()
print(my)'''


'''#copy
my = ["cars","bikes","vans","cars","helicopter"]
veh=["lorry","bicycle"]
#new=my.copy(veh)
my.extend(veh)
print(my)'''

#joins two list
'''veh=["cars","bikes","lorry","vans"]
veh1=["bicycle","scooter","trucks"]
vehicles=veh+veh1
print(vehicles)'''



