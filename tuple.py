# tuple indicates ->'( )'

'''mylist=('apple','banana','organe')
print(mylist)'''

#  A tuple is a collection which is ordered and unchangeable.
# Tuples are used to store multiple items in a single variable.

#  Tuple items are ordered, unchangeable, and allow duplicate values.

# -> Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created

'''mylist=('apple','banana','organe','apple')
print(len(mylist))
print(type(mylist))'''

'''spk1=('apple','cheery','banana','organe')
spk2=(1,2,3.4,5,7)
spk3=(True,False,True)
print(spk1,spk2,spk3)'''


'''spk=("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(spk[2:4])
print(spk[:4])
print(spk[-4:-2])

if "apple" in spk:
 print("yes,apple was present in the tuple")'''

# Once a tuple is created, you cannot change its values. 
# Tuples are unchangeable, or immutable as it also is called.

#--> remeber always that it has to convert into list and turn again into tuple 

'''#replaced values 
x=("apple", "banana", "cherry", "orange")
y=list(x)
y[1]="kiwi"
x=tuple(y)
print(x)'''

#append values
'''x=("apple", "banana", "cherry", "orange")
y=list(x)
y.append('grapes')
x=tuple(y)
print(x)'''

#adding tuple to tuple without extra variable 
'''spk=("apple", "banana", "cherry", "orange")
y=("frog","animal")
spk+=y
print(spk)'''

#remove values from tuple
'''spk=("apple", "banana", "cherry", "orange")
y=list(spk)
y.remove("apple")
spk=tuple(y)
print(spk)
'''
#delete method --> this will show an error becoz this was no longer exists
'''spk=("apple", "banana", "cherry", "orange")
del spk
print(spk)'''

# we have in packing and unpacking in tuple
'''spk=("apple", "banana", "cherry","organe","fruits")
#(green,red,yellow) =spk
#print(green,yellow)
(green,red,*violet)=spk
print(green,violet)'''


'''spk=("apple", "banana", "cherry", "orange")
for i in spk:
  print(spk)'''

#joins and multi joins 
'''spk=("apple", "banana", "cherry", "orange")
#y=spk*2
spk2=("tomato","onions")
y=spk+spk2
print(y)'''

'''spk=("apple", "banana", "cherry", "orange")
x=spk.count(2)
print(x)'''
    