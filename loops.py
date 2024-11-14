# we have two type of LOOPS
#For loop
#While loop

#while loop example
'''x=1
while x<3:
    print(x)
    x+=1'''

#while loop with break statment
'''i=1
while i<5:
    print(i)
    if i==3:
        break
    i+=1'''

'''i=2
while i<7:
    i+=2
    if i==5:
      break
    print(i)'''

'''i=0
while i<8:
    i+=1
    if i==3:
     #continue
     #break
    print(i)'''
 
# else
'''i = 1
while i<6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6") '''


#For loop
'''A for loop is used for iterating over a sequence (that is either a list, a tuple, 
a dictionary, a set, or a string).
'''

'''a=['iphone','samsung','vivo']
for x in a:
  print(x)'''

'''a=['iphone','samsung','vivo'] 
for x in a:
  if x=='samsung':
   break
  print(x) '''

'''a=['iphone','samsung','vivo']
for x in a:
  print(x)
  if x=='samsung':
   break ''' 
#continue statment
#With the continue statement we can stop the current iteration of the loop, 
# and continue with the next
'''a=['iphone','samsung','vivo']
for x in a:
 if x=='samsung':
  continue
print(x)'''
     

#range
'''for x in range(5):
  print(x) '''    

'''for x in range(2,5):
  print(x) ''' 

#range is always an Increment and now we adding with thrid parameter
'''for x in range(2,30,2):
  print(x) ''' 

'''for x in range(2,20,2):
  print(x)
else:
  print("finised")  '''

'''for x in range(2,30,3):
  if x<20:
    print(x)  '''

#break 
'''for x in range(7):
  if x==3: break
  print(x)
else:
  print("wow!")''' 

 #with nested loop
'''a=['iphone','samsung','vivo']
b=['oppo','Realme','Redmi']
for x in a:
  for y in b:
    print(x,y)  '''

#pass
'''for x in range(1,15,2):
 pass'''    