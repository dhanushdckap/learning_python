class Dhanush:
    print("Dhanush class is working....")

obj = Dhanush()


## working with function ##

class Functions:

    # Instance attribute
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show_me_what(self):
        print(f"Hello my friend {self.name} and your age must to be {self.age}")

obj = Functions("Dhanush",20)
#  Accessing class methods
obj.show_me_what()


## Inheritance ##

# Parent class

class Me(object):
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def display_my_details(self):
        print(f"Hello everyone my name is {self.name} and my id is {self.id}")

class Company(Me):
    def __init__(self,name,id,salary,post):
        self.salary = salary
        self.post = post
        Me.__init__(self,name,id)

    def employee_details(self):
        print(f"Hello Team, My name is {self.name} and My id is {self.id}. I am working as {self.post} and I am earning {self.salary}/Day")

obj = Company("Dhanush",1,100,"Intern")

obj.employee_details()
obj.display_my_details()