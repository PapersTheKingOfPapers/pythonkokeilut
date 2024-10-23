class Car:
    def __init__(self, license, topSpeed):
        self.license = license
        self.topSpeed = topSpeed
        self.topSpeedText = f"{self.topSpeed} km/h"
        self.speed = 0
        self.travelled = 0
    def printDetails(self):
        print(f"License:{self.license}\nTopSpeed:{self.topSpeedText}\nSpeed:{self.speed}\nTravelled:{self.travelled}")

car = Car("ABC-123", 142)
car.printDetails()
