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
    def printDetails(self):
        print(f"| License:{self.license} \t| Top Speed:{self.topSpeedText} \t| Speed:{self.speed}  \t| Travelled:{self.travelled}\t |")

car = Car("ABC-123", 142)
car.printDetails()
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print(f"Speed:{car.speed}")
car.accelerate(-200)
print(f"Speed:{car.speed}")

