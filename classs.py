# Object Oriented concept
"""
Write a Person class with an instance variable age, and a constructor that takes an integer, initial age, 
as a parameter. The constructor must assign iniial age to age after confirming the argument passed as  is not negative; 
if a negative argument is passed as inital age, the constructor should set age to 0 and print Age is not valid, setting age to 0.. 
In addition, you must write the following instance methods:

yearPasses() should increase the  instance variable by 1 .
amIOld() should perform the following conditional actions:
If age<13 print You are young..
If age>=13 and age<18, print You are a teenager..
Otherwise, print You are old..
"""
class Person:
    def __init__(self,initialAge):
        self.age=0
        if(initialAge>0):
            self.age = initialAge
        else:
            self.age=0
            print("Age is not valid, setting age to 0.")    
            
    def amIOld(self):
        if(self.age<13):
            print("You are young.")
        elif(self.age>= 13 and self.age<18):
            print("You are a teenager.")    
        else:
            print("You are old.")
    def yearPasses(self):
        self.age +=1

t = int(input("enter no of test cases : "))
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")

