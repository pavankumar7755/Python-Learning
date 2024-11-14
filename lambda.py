#lambda
'''A lambda function is a small anonymous function.

A lambda function can take any number of arguments, 
but can only have one expression'''

#example
#-->lambda agrument : Expression
#single argument
'''x=lambda a:a+10
print(x(4))'''

#multi arguments
'''x=lambda a,b:a*b
print(x(5,7))'''

#three statements
'''x=lambda a,b,c:a+b/c
print(type(x(2,2,2)))'''


#using with def function
'''def spk(n):
    return lambda a:a *n
spk1=spk(2)
print(spk1(4))'''