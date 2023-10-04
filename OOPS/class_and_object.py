class DCKAP_palli:
    name=""
    def __init__(self):
        print("your a member of the DCKAP PALLI")

    def student(self):
        print("your student of the DCKAP PALLI")

    def trainer(self):
        print("your the trainer in DCKAP PALLI")

dhanush = DCKAP_palli()
dhanush.name = "jeeva"
print(dhanush.name)
dhanush.student()

## the init function will run the function when the class is called.


## ----- PROBLEM-1 ----- ##

# create class called calulator. create 2 variable a and b.create a function called add,sub
# mul,div all function should take 2 variables as parameter.pass the a and b value through
# object()

class calulator:
    def __init__(self,a,b):
        self.number_1 = a
        self.number_2 = b
    def add(self):
        print(self.number_1 + self.number_2)

    def sub(self):
        print(self.number_1 - self.number_2)

    def mul(self):
        print(self.number_1 * self.number_2)

    def div(self):
        print(int(self.number_1 / self.number_2))

inputOne = int(input("set the value of the a : "))
inputTwo = int(input("set the value of the b : "))

inputs = calulator(inputOne,inputTwo)
inputs.add()
inputs.sub()
inputs.mul()
inputs.div()

## ----- instring variable and class variable ----- ##

class phone:
    charger_type = "C-TYPE" # this is class variable. it can be static and used in this class
    def __init__(self,brand,price):
        self.brand = brand # this is the instring variable it will be dyinamic and it is used in this class
        self.price = price # this is the instring variable it will be dyinamic and it is used in this class
    def display(self):
        print("brand :",self.brand)
        print("price :",self.price)
        print("charder-type :",self.charger_type)

realme = phone("realme","14000")
realme.display()

## ----- types of class method ----- ##

class laptop:
    charger_type = "C-TYPE"
    def __init__(self):
        self.brand=""
        self.price=""
    def setPrice(self,price):
        self.price = price

    def getPrice(self):
        print(self.price)

    @classmethod # this is classmethod we can change the class variable values inside this class. Without the "@classmethod"
    # it will work
    def changeChargerType(cls): # use the cls for the classmethod
        cls.charger_type = "B-TYPE"
        print("successfully charger has changed")

    @staticmethod # it is a static method is used for the displaying the unnessery methods to run
    def laptopInfo():
        print("here the laptop details")

hp = laptop()
hp.setPrice(20000)
hp.getPrice()

hp.changeChargerType()
hp.laptopInfo()

## ----- Inheritance and It's type ---- ##

class dad:
    def phone(self):
        print("dad phone")

class son(dad): ## this is know as single inheritance
    def laptop(self):
        print("sons laptop")

ram = son()
ram.laptop()
ram.phone()

class dad:
    def phone(self):
        print("dad phone")

class mom:
    def sweet(self):
        print("mom has sweet's")

class son(dad,mom): ## this is know as mulitple inheritance
    def laptop(self):
        print("sons laptop")

ram = son()
ram.laptop()
ram.phone()
ram.sweet()

## ----- multiple level inheritance and multiple inheritance----- ##

class grandfather:
    def phone(self):
        print("grandfather's phone")

class dad(grandfather):
    def money(self):
        print("Dad's money")

class sons(dad):
    def laptop(self):
        print("Son's laptop")

ram = sons()

ram.laptop()
ram.money()
ram.phone()

d1 = dad()
d1.phone()

## ----- Hierarchical inheritance ----- ##

class dad:
    def money(self):
        print("dad's money")

class son1(dad):
    pass

class son2(dad):
    pass

class son3(dad):
    pass

s2 = son2()
s2.money()

## ----- Hibirdy inheritance ----- ##

class dad:
    def money(self):
        print("dad's money")

class land:
    def important(self):
        print("important land")
class son1(dad,land):
    pass

class son2(dad):
    pass

class son3(dad):
    pass

s2 = son2()
s2.money()

## ----- Super keyword ----- ##

class a():
    def __init__(self):
        print("A")
    def display(self):
        print("your in the class a")


class b(a):
    def __init__(self):
        super().__init__() # this super key pass the exendes class init function from class A
        print("B")
    def display(self):
        print("your in the class b")

class c(b):
    def __init__(self):
        super().__init__() # this super key pass the exendes class init function from class B
        print("c")
    def display(self):
        print("your in the class c")
# obj1 = a()
obj2 = c()

## ----- Polymorphism inheritance ----- ##

def add(a=0,b=0,c=0):
    print(a+b+c)

add(40,10)

# ----- Problem-2 ----- ##

# create a class called Animal with method Sound() that prints "Animal makes sound."
# create a derived class called Dog that inherits from Animal and overrides the Sound()
# method to print "Dog Bark".Creat anthor derived class called Bird that inherits from Animals
# and Overrides the Sound() method to print "Birds sing."

class Animal:
    def Sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def Sound(self):
        print("Dog Bark")

dog = Dog()
dog.Sound()

## ----- problem-3 ----- ##

# create a base class called Shape with a method area() that returns 0.
# create a derive class called Rectangle that inherits from shape and overrides
# the area() method to calulate and return the area of the rectangle

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def area(self):
        return l * w

l = int(input("enter the length of the Rectangle : "))
w = int(input("enter the width of the Rectangle : "))

R1 = Rectangle()
R1.area()

## ----- problem-4 ----- ##

# Create a base class called Person with construtor that takes a name as parameter.
# create a derived class called student that inherits from person and constructor that takes a parameter
# called grade. Write a method in the student to display the name and grade of the student.
# Use the super keyword to achieve this.

class person:
    def __init__(self,name):
        self.name = name

class student(person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade = grade

    def display(self):
        print("student name : ",self.name)
        print("student grade : ",self.grade)

p1 = student("dhanush","A++")
p1.display()
