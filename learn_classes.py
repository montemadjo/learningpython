class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print ("Name: ", self.name, ", Salary: ", self.salary)

emp1 = Employee("Mićko", 2000)
emp2 = Employee("Bućko", 4000)

print(Employee.__bases__)
emp1.displayEmployee()
emp2.displayEmployee()