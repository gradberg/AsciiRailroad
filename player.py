
#import libtcodpy as libtcod
import Map as MOD_MAP
import Utilities
import logging

class Player:
    def __init__(self, x,y, train, car):        
        self.X = x
        self.Y = y
        self.OnCar = car
        
    def GetLocation(self):
        if self.OnCar is None:
            return self.X, self.Y
        else:
            return self.OnCar.X, self.OnCar.Y
            
    def GetTrain(self):
        if (self.OnCar is None): return None
        return self.OnCar.ParentTrain 

    def Move(self, map, trains, direction):    
        if self.OnCar is None:
            return self.MoveOnMap(map, trains, direction)
        else:
            return self.MoveOnTrain(map, trains, direction)
    
    def MoveOnTrain(self, map, trains, direction):
        if (direction == 'W'):
            moveDirection = Utilities.GetWestFromDirection(self.OnCar.Direction)
            return self.MoveOnMap(map, trains, moveDirection)
            
        elif (direction == 'E'):
            moveDirection = Utilities.GetEastFromDirection(self.OnCar.Direction)
            return self.MoveOnMap(map, trains, moveDirection)
            
        elif (direction == 'N'): # move up one car
            carIndex = self.GetTrain().GetCarIndex(self.OnCar)
            if (carIndex == 0): return False
            self.OnCar = self.GetTrain().Cars[carIndex - 1]
            return True
            
        elif (direction == 'S'): # move down one car
            carIndex = self.GetTrain().GetCarIndex(self.OnCar)
            if (carIndex >= len(self.GetTrain().Cars) - 1): return False
            self.OnCar = self.GetTrain().Cars[carIndex + 1]
            return True
        
        else:        
            return False
        
    def MoveOnMap(self, map, trains, direction):        
        # Get coordinates of square that will be moved on to
        offsetX, offsetY = Utilities.GetOffsetsForDirection(direction)
        myX, myY = self.GetLocation() # makes it work whether you're on a car or not        
        x = myX + offsetX
        y = myY + offsetY
        
        # Verify this is not off the edge of the map.
        if (x < 0 or
            x >= MOD_MAP.WIDTH or
            y < 0 or
            y >= MOD_MAP.HEIGHT):
            return False
        
        # If a train car, put the player on that train car instead
        train, car = FindTrainAtLocation(trains, x, y)        
        if train is None:
            self.X = x
            self.Y = y
            self.OnCar = None
        else:
            self.X = -1
            self.Y = -1
            self.OnCar = car        
            #logging.debug("on car [" + car.Name + "] at [" + `x` + "," + `y` + "]")
    
        return True
        
        
    def Activate(self, map):
        # Only used for On Foot right now.
        if (not self.OnCar is None): return self.ActivateTrainCar(map)
        
        tile = map[self.X][self.Y]
        switch = tile.Switch
        if (switch is None): return False
        
        if (not switch.ControlTile is tile): return False
        switch.Activate()
        return True

    def ActivateTrainCar(self, map):
        if (not self.OnCar.Engine is None): return self.OnCar.Engine.Activate()
        return False
        

def FindTrainAtLocation(trains, x, y):
    for train in trains:
        for car in train.Cars:
            if (car.X == x and car.Y == y):
                return train, car
    
    return None, None

    