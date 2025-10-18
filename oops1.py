class employee:
    def __init__(self, name, age, salary):
        print('start constructor')
        self.name = name
        self.age = age
        self.salary = salary
        print('end constructor')

    def display(self):
        print ('start method')
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

emp1 = employee("Alice", 30, 70000)
print(type(emp1))