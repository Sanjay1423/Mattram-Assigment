

class Person:
    avg_income = 15000
    nationality = "Indian"

    def __init__(self, name, age, sex, city):
        self.name = name
        self.age = age
        self.sex = sex
        self.city = city

    # normal method which holds the object name as a first argument as 'self'
    def person_bio(self):
        bio = f'{self.name} is {self.age} years old living in {self.city} and {self.name} is a {self.sex}'
        return bio

    # with class method we can access and modify the class variable
    @classmethod
    # We can access with the argument of 'cls' which holds the class name
    def change_avg_income(cls, income):
        new_avg_income = sum(income)/len(income)
        cls.avg_income = new_avg_income
        return cls.avg_income

    # Static method doesnt need a class name(cls) or object name(self)
    @staticmethod
    def driving_eligibility(driving_license):
        if driving_license == True:
            return "You are eligible for driving"
        return "You are not eligible for driving"


person1 = Person('Sanjay', 19, 'male', 'Chennai')
person2 = Person('Sriram', 20, 'Male', 'Banglore')

# Accessing Class method change_avg_income() with class name
Person.change_avg_income([12000, 10000, 15000, 17000])

# Accessing the static method driving_elgiblilty()
person1.driving_eligibility(False)
