
# Parent Class
class bike:
    def __init__(self, color, CC, mileage, year_of_manufactured):
        self.color = color
        self.CC = CC
        self.mileage = mileage
        self.color = color
        self.year_of_manufactured = year_of_manufactured

    def engine(self):
        return f"The engine is {self.CC}"

# parent class


class electric_vehicle:
    def __int___(self, charging_time):
        self.charging_time = charging_time

    def charging(self):
        return f"It takes {self.charging_time} to charge"


# Child Class of bike
# This class falls under the single level inheritence
class yamaha(bike):
    def __init__(self, color, CC, mileage, year_of_manufactured, type_of_engine):
        # super() method is used to get the attributes of the parent class
        super().__init__(color, CC, mileage, year_of_manufactured,)
        self.type_of_engine = type_of_engine


# Child class of yamaha which inherits the attributes and methods of both bike and yamaha
# This is class falls under the mutlevel inheritance
class R15(yamaha):
    def __init__(self, color, CC, mileage, year_of_manufactured, type_of_engine, top_speed):
        super().__init__(CC, mileage, year_of_manufactured, type_of_engine, top_speed)
        self.top_speed = top_speed

# This class falls under the mutliple inheritence
# This class inherits bike and electric_vehicle class at a same time


class ola(bike, electric_vehicle):
    def __init__(self, color, CC, mileage, year_of_manufactured, charging_time):
        bike.__init__(self, color, CC, mileage, year_of_manufactured)
        electric_vehicle.__init__(self, charging_time)


# bike1 object used to access the yamaha class
bike1 = yamaha('red', 150, 40, 2019, '2 stroke')
bike1.engine()


# bike2 object used to access the R15 class
bike2 = R15('blue', 200, 35, 2020, '4 stroke', 150)
bike2.top_speed

# bike3 object used to access the ola class
bike3 = ola('black', 100, 45, 2022, 3)
print(bike3.charging())