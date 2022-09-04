# Dunder or Magic Methods

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f'{self.name} and {self.salary}'

    def __repr__(self):
        return f'Employee({self.name},{self.salary})'

    # __add__ can perform addition operation in a class
    def __add__(self, other):
        return self.salary + other.salary 

    #  __ sub__ can perfom subtraction operation in a class
    def __sub__(self, other):
        return self.salary - other.salary

    # __add__ can perform equal to  operation in a class
    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False

    # __len__ can find a length of the given string in a class
    def __len__(self):
        return len(self.name)

    # __getitem__ can perform slicing operation in a class
    def __getitem__(self, key):
        return self.name[key]

    # __contain__ to perform in operation in a class
    def __contain__(self, value):
        if value in self.name:
            return True
        else:
            return False


emp1 = Employee('Sanjay', 15000)
emp2 = Employee('Prakash', 30000)

print(emp1 + emp2)
print(emp1 - emp2)
print(emp1 == emp2)
print(len(emp1))
print(emp1[2])
print('s' in emp2)

