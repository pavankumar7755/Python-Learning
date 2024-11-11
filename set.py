# set Represent ' {} '
# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# Set items are unordered, unchangeable, and do not allow duplicate values.

#unordered 
'''spk={'apple','organe','cherry'}
print(type(spk))
print(spk)
'''

#duplicated not allowed
'''spk={'apple','organe','cherry','apple'}
print(spk)'''
#True and 1 is considered the same value
#1 will not executed
'''set={'apple','organe',True,1,2}
print(set)'''

#booelan fuction
'''set=('apple','samsung','realme')
print('realme' in set)'''

#adding new item & two sets

'''set={'apple','samsung','realme'}

#set.add('vivo')
#print(set)
set1={'vivo','oppo','motorola'}
set.update(set1)
print(set)
'''
#adding set & list

'''set={'apple','samsung','realme'}
set1=['vivo','oppo']
set.update(set1)
print(set)'''

'''#remove or discard or pop --> for delete from set
set={'apple','samsung','realme'}
#set.remove('apple')
#set.discard('apple')
#x=set.pop()
print(x)'''

#clear the set
'''set={'apple','samsung','realme'}
set.clear()
print(set)'''

#delete
'''set={'apple','samsung','realme'}
del set
print(set)'''


#joins
'''set={'apple','samsung','realme'}
set1={'vivo','oppo'}
#set3=set.union(set1)
#set3=set | set1
print(set3)'''
#multi set to join
'''set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
#x=set1.union(set2,set3,set4)
x=set1 | set2 | set4
print(x)'''

#join set with tuple . with NO Duplicates
'''set={"iphone","samsung","vivo"}
set1=("vivo","oppo")
x=set.union(set1)
print(x)'''

#upadte method in One set
'''set={"iphone","samsung","moto"}
set1=("vivo","oppo")
set.update(set1)
print(set)'''

#intersection or '&' it show only duplicates or common value
'''set={"iphone","samsung","vivo"}
set1={"vivo","oppo"}
#x=set.intersection(set1)
x= set&set1
print(x)'''

#intersection with update
'''set={"iphone","samsung","vivo"}
set1={"vivo","oppo"}
set.intersection_update(set1)
print(set)'''

#same values true =1 and false = o
'''set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)'''


#difference
'''set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)'''

#difference with operators
'''set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1-set2

print(set3)'''


#symmetric Difference
set={'iphone','pixels','vivo'}
set1={'samsung','oppo','realme','iphone'}
set2=set.symmetric_difference(set1)
print(set2)