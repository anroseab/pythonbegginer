class Empl:
    company = 'learn2code'

    def __init__(self, name, age, salary, desig, dep, resp, cpu, gpu, ram):
        self.name = name
        self.age = age
        self.salary = salary
        self.email = self.generateemail(Empl)
        self.job = Empl.Job(desig, dep, resp)
        self.computer = Empl.Computer(cpu, gpu, ram)

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

    class Job:
        def __init__(self, designation, department, responsibility):
            self.designation = designation
            self.department = department
            self.responsibility = responsibility

        def showInfo(self):
            print(self.designation, self.department, self.responsibility)

    class Computer:
        def __init__(self, cpu, gpu, ram):  # ✅ fixed __init__
            self.cpu = cpu
            self.gpu = gpu
            self.ram = ram

        def showInfo(self):
            print(self.cpu, self.gpu, self.ram)

# Create an object
obj = Empl('john', 38, '$1234', 'Manager', 'IT', 'service', 'i7', 'gtx1016', 20)

# Show all info
obj.showInfo()
obj.job.showInfo()
obj.computer.showInfo()
