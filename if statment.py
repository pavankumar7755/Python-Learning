#  An "if statement" is written by using the if keyword.
#Indentation
'''Python relies on indentation (whitespace at the beginning of a line) 
to define scope in the code. 
Other programming languages often use curly-brackets for this purpose.'''

#without indentation ,shows error
'''a=34
b=32
if a>b:
print("yes")'''

#with indentation
'''a=34
b=32
if a>b:
    print("yes! correct")'''

#Elif 
'''The elif keyword is Python's way of saying 
"if the previous conditions were not true, then try this condition".'''

#elif

'''a=32
b=34
if a>b:
    print("a is big")
elif b>a:
    print("b is bigger")   ''' 

#else
'''The else keyword catches anything which isn't 
caught by the preceding conditions.'''

'''a=45
b=37
if a==b:
    print("equal")
elif a<=b:
    print("not equal")    
else:
    print("a is  big")    '''

# You can also have an else without the elif:

'''a=57
b=89
if a>b:
    print("not big")
else:
    print("big") '''   

#Short hand if

a=34
b=75
#if b>a: print("yuuup!") 
#print("no") if  a==b else print("yoo!")
#print("aa") if a>b else print("equal") if a==b else print("b is greater")

#multi Statement
a=87
b=78
c=87
'''if a>b and c==a:
    print("Prefect")'''
'''if c==b or c>b:
    print("yooo!")'''

'''if not b>a:
    print("super!")'''

#NESTED IF Statement
'''a=24
if a>12:
    print("a")
    if a>22:
        print("equal")
    else:
        print("b")'''    

#pass with if Statement
a=34
b=34
if c==a:
    pass
else:
    ("equal")