class Empl:
    company = 'learn2code'

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.email = self.generateemail(Empl)
    def generateemail(self, cls):
        return f'{self.name}@{cls.company}.com'

    def showInfo(self):
        print(self.name, self.age, self.salary, self.email)

    @classmethod
    def changeCompanyName(cls, newName):
        cls.company = newName

    @staticmethod
    def info():
        print('This is a class for creating employee object and the IT requirements')

# Create an object
obj = Empl('john', 38, '$1234')

# Show all info
obj.showInfo()
