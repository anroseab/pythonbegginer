class Employee:
   
    def ShowEmployee(self):
        print('john','39','$123456789')
obj=Employee()
obj.ShowEmployee()



class Emplo:
    def  __init__ (self) :
        print('new object craeted')
obj=Emplo()




class Empl:

    def __init__(self, name, age, salary,email):
        self.name = name
        self.age = age
        self.salary = salary
        self.email = email

    def showInfo(self):
        print(self.name, self.age, self.salary, self.email)

# Create an object
obj = Empl('john', 38, '$1234','@gmail.com')

# Show all info
obj.showInfo()



