'''A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.'''

#n Python a function is defined using the 'def' keyword
#Calling function
'''def spk():
    print("helo this is function")
spk()  '''  

#Arguments
#Information can be passed into functions as arguments.

'''def spk(fname,lname):
    print(fname+lname+"!")
spk("pavan","kumar")
spk("sunny","kumar")
spk("sandhi","pavan")''' 


#Parameter or Argument
#The terms parameter and argument can be used for the same thing: 
# information that are passed into a function.
#From a function's perspective:

'''A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called'''

'''def spk(fname,lname):
    print(fname+" "+lname)
spk("pavan","kumar")
spk("sandhi","sunny")    '''

#Arugment (*args)
'''def spk(*fname):
    print("i am "+fname[2])
spk("pavan","kumar","sandhi")  '''  


'''def spk(fname,lname,iname):
    print("my name is "+fname)
spk(fname="pavan",lname="kumar",iname="sandhi") '''   

#kwargs
'''def spk(**name):
    print("my name was"+name["lname"])
spk(fname="pavan",lname="sandhi") '''   

#Default parameter
'''def spk(country='norway'):
    print("my country is " + country)
spk('india')
spk('AMERICA') 
spk()   
spk('RUSSIA')
spk()
'''

#Passing a list as an Argument
'''def spk(food):
    for x in food:
        print(x)
fruits=['apple','organe','banana']     
spk(fruits)  ''' 

#return
'''def spk(x):
    return 5*x
print(spk(2))
print(spk(3))
print(spk(4))
print(spk(5))'''

#pass
'''def spk():
    pass'''


#positional -Only Agrument
'''def spk(x,/):
    print(x)
spk(3)'''    

#keyword-only Agrument
'''def spk(*,x):
    print(x)
spk(x=3)'''    

#combinational positional and keyword agrument
def spk(a,b,/,*,c,d):
    print(a+b+c+d)
spk(1,2,c=4,d=8)    


#recursion
