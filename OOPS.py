'''OPPS-object oriented Programming System.
everthing is object(ex: pen,bicycle,human)
every object has properties and behaviour
for properties-->human is object and his properties is (name,gender,height,weight)
    behaviour -->human is object and his Behaviour is (what u doing,what action )'''

#properties-->variable or attributes
#behaviour --> method or procedures 

#object has attributes with methods
#class is collection of objects
#class is blurprint for object

#example

'''class spk:
    a=10
    b=20
obj=spk()
print(obj.a)
'''

#with methods
'''class sampleclass:
    def samplemethod(self):
        print("this method is created to demonstrat")'''

#"(__init__())"All classes have a function called __init__(), which is always executed when the class is being initiated.
#Note: The __init__() function is called automatically every time the class is being used to create a new object.
'''class myclass:
    x=5
p1=myclass()
print(p1.x)  '''  


'''class BankAccount:
    def __init__(self,accountNo,acoountName,ifsecode,balance):
        self.accountNo=accountNo
        self.accountname=acoountName
        self.ifsecode=ifsecode
        self.balance=balance
    def display(self):
        print(self.accountNo,self.accountname,self.ifsecode,self.balance)
obj1=BankAccount(12345,"pavan","PK284J",884)
obj1.display()     
        '''


class BankAccount:
    def __init__(self,accountNo,acoountName,ifsecode,balance):
        self.accountNo=accountNo
        self.accountname=acoountName
        self.ifsecode=ifsecode
        self.balance=balance
    def withdraw(self,amount):
        self.balance-=amount
        print(self.balance)
    def deposit(self,amount):
        self.balance+=amount
        print(self.balance)
    def checkbalance(self):
       print(self.balance,"this is total")
obj1=BankAccount(1234,"pavan","mj234",8884)
obj2=BankAccount(2345,"sandhi","mj345",983)

obj2.deposit(500)
obj2.withdraw(37)
obj1.withdraw(14)
obj1.deposit(49)
obj1.checkbalance()
obj2.checkbalance()
print("this is obj2",obj2.accountname)



     
             

