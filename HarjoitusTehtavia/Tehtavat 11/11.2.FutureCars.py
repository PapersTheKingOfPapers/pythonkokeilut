class Car:
    def __init__(self, license, topSpeed):
        self.license = license
        self.topSpeed = topSpeed
        self.topSpeedText = f"{self.topSpeed} km/h"
        self.speed = 0
        self.travelled = 0
    def accelerate(self, acceleration):
        self.speed += acceleration
        if self.speed >= self.topSpeed:
            self.speed = self.topSpeed
        elif self.speed <= 0:
            self.speed = 0
    def drive(self, hours):
        self.travelled += self.speed*hours
    def return_details(self):
        return f"| License:{self.license} \t| Top Speed:{self.topSpeedText} \t| Speed:{self.speed} km/h \t| Travelled:{self.travelled} km \t| "
    def print_details(self):
        print(self.return_details())

class ElectricCar(Car):
    def __init__(self, license, topSpeed, batteryCap):
        super().__init__(license, topSpeed)
        self.batteryCap = batteryCap
    def accelerate(self, acceleration):
        super().accelerate(acceleration)
    def drive(self, hours):
        super().drive(hours)
    def return_details(self):
        return f"{super().return_details()}Battery Capacity: {self.batteryCap} kWh \t| "
    def print_details(self):
        print(self.return_details())

class CarbonCar(Car):
    def __init__(self, license, topSpeed, gasTankSize):
        super().__init__(license, topSpeed)
        self.gasTankSize = gasTankSize
    def accelerate(self, acceleration):
        super().accelerate(acceleration)
    def drive(self, hours):
        super().drive(hours)
    def return_details(self):
        return f"{super().return_details()}Gas Tank Size: {self.gasTankSize} Liters \t| "
    def print_details(self):
        print(self.return_details())


cars = []
cars.append(ElectricCar("ABC-15",180,52.5))
cars.append(CarbonCar("ACD-123",165,32.3))

for car in cars:
    car.accelerate(60)
    car.drive(3)

for car in cars:
    car.print_details()

