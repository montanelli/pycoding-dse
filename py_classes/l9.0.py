# object oriented programming
# Class - a template
# Method or Message - A defined capability of a class (portion of code, function)
# Field or attribute or property - A bit of data in a class
# Object or Instance - A particular instance of a class

# inheritance
# When we make a new class - we can reuse an existing class and inherit all the capabilities of an existing class and then add our own little bit to make our new class
# Write once - reuse many times
# The new class (child) has all the capabilities of the old class (parent) - and then some more
# ‘Subclasses’ are more specialized versions of a class, which inherit attributes and behaviors from their parent classes, and can introduce their own.

import sys


class Vehicle:
    wheels = None
    brand = None
    model = None
    color = None
    engineSize = None
    registrationPlate = None
    fuel = None

    fuels = ["gas", "diesel", "petrol", "hybrid", "electric"]

    # constructor method
    # When the object is constructed, the __init__ method is called to allocate and initialize the attributes that require to receive a value to create a proper instance of the class
    def __init__(self, brand=None, model=None, color=None, engineSize=None):
        self.brand = brand
        self.model = model
        self.color = color
        self.engineSize = engineSize

    # destructor method
    # When the object is destroyed, the __del__ method is called to de-allocate the memory assigned to the object
    def __del__(self):
        if self.registrationPlate is None:
            print("I destroyed", self.color, self.brand, self.model)
        else:
            print(
                f"I destroyed the {self.color} {self.brand} {self.model} with plate {self.registrationPlate}"
            )

    # further methods
    def showDescription(self):

        if self.registrationPlate is None:
            print("This vehicle is a", self.color, self.brand, self.model)
        else:
            print(
                f"This is the {self.color} {self.brand} {self.model} with plate {self.registrationPlate}"
            )

    def setColor(self, color):
        self.color = color

    def setFuel(self, fuel):
        global fuels

        if fuel in fuels:
            self.fuel = fuel

    def setPlate(self, thePlate):
        self.registrationPlate = thePlate

    def setDescription(self, theModel, theBrand, theEngineSize):
        self.brand = theBrand
        self.model = theModel
        self.engineSize = theEngineSize

    def printWheels(self):
        print(f"this vehicle has {self.wheels} wheels.")


class Truck(Vehicle):
    wheels = 6
    fuel = "diesel"


class Motorcycle(Vehicle):
    wheels = 2


class Car(Vehicle):
    wheels = 4
    parkAssist = None

    def hasParkAssist(self, parkAssist):
        if parkAssist:
            self.parkAssist = True
        else:
            self.parkAssist = False


# main code
car1 = Car()
car1.setColor("green")
car1.setPlate("FH 348 ER")
car1.setDescription("Golf", "Volkswagen", 2000)
car1.showDescription()

# The dir() command lists capabilities/methods of an object
print(dir(car1))

myTruck = Truck()
myTruck.printWheels()

car2 = Car()
car2.setColor("blue")
car2.setPlate("GG 566 XC")
car2.printWheels()

car3 = Car("Volvo", "XC60", "black")
car3 = 34

sys.exit()
