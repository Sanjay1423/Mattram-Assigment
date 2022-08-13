string, lst = " ", []   # built-in classes

# Class is skeleton or blueprint for a object


class Person:     # class Name
    species = "human"

    def __init__(self, name, age, sex, city):  # Constructor is default method in class
        self.name = name
        self.age = age     # Class Attribute
        self.sex = sex
        self.city = city   # "self" is an common argument to hold the different object name

    def person_bio(self):
        bio = f'{self.name} is {self.age} years old living in {self.city} and {self.name} is a {self.sex}'
        return bio

    def eligibility(self):   # class Method
        if self.age >= 18:
            return f'{self.name} is eligible'
        else:
            return f'{self.name} is not eligible'

# we can create multiple objects from one class


person1 = Person('Sanjay', 19, 'male', 'Chennai')   # Person object1
person2 = Person('Ramya', 14, 'female', 'Hyderabad')  # Person object2

print(Person.species)
print(person1.species)
person2.species = 'mammals'
print(person2.species)
