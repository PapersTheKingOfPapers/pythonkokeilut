import random
from datetime import datetime

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
        print(f"| License:{self.license} \t| Top Speed:{self.topSpeedText} \t| Speed:{self.speed} km/h  \t | Travelled:{self.travelled} km  \t |")
    def return_travelled(self):
        return self.travelled

class Race:
    def __init__(self, name, length, cars):
        self.name = name
        self.length = length
        self.cars = cars
        self.hour = 0
    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
        self.hour += 1
    def print_state(self):
        for car in self.cars:
            car.printDetails()
    def race_over(self):
        state = False
        for car in self.cars:
            if car.return_travelled() >= self.length:
                state = True
            else:
                state = False
        return state

maxRacers = 10
racersAmount = 1
racers = []

while racersAmount <= maxRacers:
    racers.append(Car(f"ABC-{racersAmount}",random.randint(100,200)))
    racersAmount += 1

r = Race("Great Python Demolition Derby",8000,racers)

raceOngoing = True
print(f"Welcome to the {r.name} of {datetime.year}. The race will go to a length of {r.length} kilometers!")
print(f"Let the {r.name} begin!")
while raceOngoing:
    if r.hour % 10 == 0:
        print(f"And the current state of the race at {r.hour} hours of the race is as follows:")
        r.print_state()
    r.hour_passes()
    if r.race_over() == True:
        raceOngoing = False
print(f"And that's that folks! We have a winner!")
r.print_state()