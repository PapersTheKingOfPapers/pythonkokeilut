class Elevator:
    def __init__(self, lowest, highest, number):
        self.lowest = lowest
        self.highest = highest
        self.currentFloor = lowest
        self.number = number
    def to_floor(self, floor):
        while self.currentFloor != floor:
            if floor > self.currentFloor:
                self.floor_up()
            elif floor < self.currentFloor:
                self.floor_down()
    def floor_up(self):
        if self.currentFloor < self.highest:
            self.currentFloor += 1
            print(f"Elevator {self.number} moved to floor {self.currentFloor}")

    def floor_down(self):
        if self.currentFloor > self.lowest:
            self.currentFloor -= 1
            print(f"Elevator {self.number} moved to floor {self.currentFloor}")

class House:
    def __init__(self, lowest, highest, elevatorAmount):
        self.lowest = lowest
        self.highest = highest
        self.elevators = []
        while len(self.elevators) < elevatorAmount:
            self.elevators.append(Elevator(self.lowest,self.highest,len(self.elevators)+1))

    def use_elevator(self, elevatorNumber, targetFloor):
        print("-|-")
        self.elevators[elevatorNumber - 1].to_floor(targetFloor)
    def fire_alarm(self):
        i = 0
        while i < len(self.elevators):
            self.use_elevator(i,self.lowest)
            i += 1

h = House(-1,4,2)
h.use_elevator(1,2)
h.use_elevator(2,3)
h.fire_alarm()