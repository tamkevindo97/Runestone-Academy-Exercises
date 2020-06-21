class Automobile:

    def __init__(self, make, gas_tank, wheels):
        self.make = make
        self.gas_tank = gas_tank
        self.wheels = wheels

    def numberofWheels(self):
        return str(self.wheels)

    def typeofAutomobile(self):
        return self.make

    def addGas(self, gallons):
        self.gas_tank = gallons + self.gas_tank
        return str(gallons)

    def gasTotal(self):
        return str(self.gas_tank)

class Car(Automobile):

    def __init__(self, make, gas_tank, wheels = 4):
        super().__init__(make, gas_tank, wheels)


class Bike(Automobile):

    def __init__(self, make, gas_tank, wheels = 2):
        super().__init__(make, gas_tank, wheels)

toyota = Car("Toyota", 6)
print("The make of this car is " + toyota.typeofAutomobile())
print("Number of wheels " + toyota.numberofWheels())
print("Added gas: " + toyota.addGas(2))
print("Total gas: " + toyota.gasTotal())


Harley = Bike("Harley", 3)

print("The make of this car is " + Harley.typeofAutomobile())
print("Number of wheels " + Harley.numberofWheels())
print("Added gas: " + Harley.addGas(3))
print("Total gas: " + Harley.gasTotal())
