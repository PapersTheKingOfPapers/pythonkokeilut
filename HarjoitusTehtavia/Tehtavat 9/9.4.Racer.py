import random
class Car:
    def __init__(self, license, topSpeed):
        self.license = license
        self.topSpeed = topSpeed
        self.topSpeedText = f"{self.topSpeed} km/h"
        self.speed = 0
        self.travelled = 0
    def accelerate(self, acceleration: int):
        self.speed += acceleration
        if self.speed >= self.topSpeed:
            self.speed = self.topSpeed
        elif self.speed <= 0:
            self.speed = 0
    def drive(self, hours):
        self.travelled += self.speed*hours
    def printDetails(self):
        print(f"| License:{self.license} \t| Top Speed:{self.topSpeedText} \t| Speed:{self.speed}  \t| Travelled:{self.travelled}\t |")

maxRacers = 10
racersAmount = 1
racers = []

while racersAmount <= maxRacers:
    racers.append(Car(f"ABC-{racersAmount}",random.randint(100,200)))
    racersAmount += 1

raceGoing = True
while raceGoing:
    for obj in racers:
        obj.accelerate(random.randint(-10,15))
        obj.drive(1)

    for obj in racers:
        if obj.travelled >= 10000:
            raceGoing = False

for obj in racers:
    obj.printDetails()