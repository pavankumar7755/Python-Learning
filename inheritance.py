#inheritance
#Inheritance allows us to define a class that inherits all the methods and properties from another class
#Parent class is the class being inherited from, also called base class.

#Child class is the class that inherits from another class, also called derived class

#type of Inheritance
'''1)Single inhertiance
2)multiple inheritance
3)Multilevel inheritance
4)Hierarchical inheritance
5)Hybrid inheritance'''

#single inheritance

'''class parent:
    def method1(self):
        print("i am  a parent")
class child(parent):
    def method2(self):
        print(" i am child")
child1=child()
child1.method2()  
child1.method1()  
parent1=parent()
parent1.method1()'''
#parent1.method2()-- it doesn't becoz partent class can't use there child class but class can use parent class

#multiple inheritance

'''class father:
    def method1(self):
        print("i am a father")
class mother():
    def method2(self):
        print(" i am a mother")
class child(father,mother):
    def method3(self):
        print("i am a child")
obj1=child()
obj1.method2()  
obj1.method1()  
print(child.__mro__)  '''    

#multilevel inheritance
'''class grandfather():
    def method1(self):
        print(" i am grand father")
class father(grandfather):
    def method2(self):
     print("i am father")
class child(father):
    def method3(self):
        print("i am child")
obj=child()
obj.method2()
obj.method3()'''     

#hierarchical inheritance

'''class parent:
    def method1(self): 
        print("i am parent to")
class fchild(parent):
    def method2(self):
        print(" i am a fchild")
class schild(parent):
    def method2(self):
        print("i am schild ")        
fchild=fchild()
fchild.method2()
fchild.method1()  '''  

#Hybrid inheritance
x="40"
y=8
c=x*y
print(c)
              