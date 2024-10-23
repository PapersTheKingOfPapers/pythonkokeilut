class Elevator:
    def __init__(self, lowest, highest):
        self.lowest = lowest
        self.highest = highest
        self.currentFloor = lowest
    def to_floor(self, floor):
        difference = 0
        while self.currentFloor != floor:
            if floor > self.highest:
                floor = self.highest
            elif floor < self.lowest:
                floor = self.lowest
            difference = self.currentFloor - floor
            if difference >= 1:
                self.floor_down()
            elif difference <= -1:
                self.floor_up()
    def floor_up(self):
        if self.currentFloor + 1 <= self.highest:
            self.currentFloor += 1
            print(f"Moved to floor {self.currentFloor} from floor {self.currentFloor-1}")

    def floor_down(self):
        if self.currentFloor - 1 <= self.lowest:
            self.currentFloor -= 1
            print(f"Moved to floor {self.currentFloor} from floor {self.currentFloor+1}")

e = Elevator(-2,10)
e.to_floor(4)