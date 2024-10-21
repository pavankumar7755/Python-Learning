# string may be in single quote or double quote

#print("helo world")

'''a='hi pavan'
print(a)'''

#a="""Strings are very versatile and widely 
   #used in Python for handling text and data"""

#print(a)


#a='hi' * 4
#print(a)
#print([a])

#b='pavan'
#print(b[2])       #it gives index of string.it index start from 0.


'''c='hola'
print(len(c))      #it gives length of the string
print(max(c))      #it give alphebetical order max
print(min(c))  '''    #it give alphebetical order min


# check string with if condition
'''txt='the best thing in the life is free'
if "free" in txt:
   print("yes, 'free' is present")'''

#check sting true or flase keyword is ('in')
'''txt='the best thing in the life is free'
print('free' in txt)  '''


#check sting true or flase keyword is ('not in')
'''txt='the best thing in the life is free'
print('expensive' not in txt)'''

# check string with if condition with NOT present
'''txt='the best thing in the life is free'
if 'expensive' not in txt:
    print("no,'expensive' is NOT present")'''


#slicing   -->calling sting with index 
'''a='hola world'
print(a[2:6]) 
print(a[:3])
print(a[5:10])
print(a[-5:-2])
print(a[0:])'''

#modift string

'''a=" holS,world!  "
print(a.upper())
print(a.lower())
print(a.strip())'''  #removing whitespace from beginning or end

'''b="hola world"
print(b.replace("h","j")) '''   #replace sting with words


#c="hola pavan"
#print(c.split()) #split separteing sentence into diffrent strings

#string concatenation --> combine with words

'''a='hola'
b='pavan'
c=a+b
print(c)
'''

'''a='hola'
b='world'
#c=a+","+b     #method adding comma for it word
#c=a+" "+b     #method spacing for word
print(c)'''


#string format  
# this is wrong format
'''a = 24
b = "my name is pavan,my age is " 
c=b+a
print(c)'''

#right format to do 

"""An f-string (formatted string literal) in Python is a convenient way to embed expressions inside string literals using curly braces {}. Introduced in Python 3.6, f-strings allow you to directly insert variables, expressions, or function 
calls within strings, making formatting easier and more readable"""
#example 1
'''age = 24
txt  = f"my name is pavan,my age is {age}"
print(txt)

#example 2
name = 'pavan'
age = 24
village = 'akividu'
intro = f"my name is {name} and i am {age} years old from {village} village"
print(intro)

#example 3
a= 5
price = f"the amount u have to pay {a}"
print(price)

#example 4
cost=f"ur room tent due is {30000 * 2}"
print(cost)
'''

#Escape character 
#An escape character is a backslash \ 
# followed by the character you want to insert.
#
'''txt = "my name is \"pavan\" "
print(txt)'''
#\n for new line
"""txt = "hello \nworld "
print(txt)
#\\ for backslash
txt = "This will insert one \\ (backslash)."
print(txt) 
#\r for carriage return
txt = "Hello\rWorld!"
print(txt) 
#\b for backspace
#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 
#\t for tab
txt = "Hello\tWorld!"
print(txt) 

#centre
txt = "banana"
x = txt.center(20)
print(x)







#Method	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning"""