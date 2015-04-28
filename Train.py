import Utilities
import Map

DRAG = 0.02

#
#
# Represents one or more cars on the tracks, consisting of multiple cars
class Train:
    # Trains are not valid without at least one car, so you must provide a first car
    # to the constructor
    def __init__(self, firstCar):
        # Cars are explicitly in order, and are moved and such in that fashion.
        self.Cars = []
        self.Cars.append(firstCar)
        firstCar.ParentTrain = self
        
        # Cars no longer have a direction pointing (because it is darn near unmanagable
        # to keep track of each cars direction, which could point EITHER WAY, and then
        # mesh that into the train object. Its terrible. So now only Trains keep track
        # of direction, and in that case only the front direction and the back direction.
        # If merging with another train, the only check that need be done is that you are
        # not hitting a car on a + track (which perhaps for now will not be allowed), 
        
        # Cars have their own directional pointing (which on a train will always be normalized
        # to point FOWARD). Unfortunately cars must retain a direction, because otherwise it
        # is infeasible to detach a car from a train and re-establish which direction the front
        # or back is (without referring to the track and making guesses)
        
        # The train doesn't need its own directions stored, because those are just the
        # first and last car. But as long as i always normalize all directions when cars
        # are add, all of the cars will be facing the right way.
        #self.FrontDirection = firstCar.Direction
        # For the back direction, it IS STILL POINTING FORWARD. So a one car train will 
        # have identical front and back directions
        #self.BackDirection = firstCar.Direction
        
        # Positive speed represents the front car 'pulling' all the cars along its path 
        # in its direction.
        # Negative speed represents the back car 'pulling' all the cars along its path
        # in the __REVERSE__ of its direction (because its current direction has been
        # normalized to point 'foward' like the rest of the cars)
        self.Speed = 0.0
        
        self.HasCollided = False # Used for movement/collision detection
        
        self.HasCrashed = False # Temporary flag for handling bad situations.
    
    #def GetFrontCarLocation(self):
    #    return self.Cars[0].X, self.Cars[0].Y
    
    def PrefixCar(self, car):    
        car.Direction = Utilities.NormalizeDirection(self.GetFrontDirection(), car.Direction)
        self.Cars.insert(0, car)
        car.ParentTrain = self        
    
    def AppendCar(self, car):
        car.Direction = Utilities.NormalizeDirection(self.GetBackDirection(), car.Direction)
        self.Cars.append(car)
        car.ParentTrain = self
        
    def RemoveCar(self, car):
        self.Cars.remove(car)
        car.ParentTrain = None
      
    def IsSingleCar(self):
        return len(self.Cars) == 1
        
    def GetFrontCar(self):
        return self.Cars[0]
        
    def GetBackCar(self):
        return self.Cars[len(self.Cars) - 1]
    
    # The train doesn't need its own directions stored, because those are just the
    # first and last car. But as long as i always normalize all directions when cars
    # are add, all of the cars will be facing the right way.
    def GetFrontDirection(self):
        return self.GetFrontCar().Direction
    
    # For the back direction, it IS STILL POINTING FORWARD. So a one car train will 
    # have identical front and back directions    
    def GetBackDirection(self):
        return self.GetBackCar().Direction
        

    def GetCarIndex(self, searchCar):
        index = 0
        for car in self.Cars:
            if (car is searchCar): return index
            index += 1
            
        return -1
        
    def DoSpeedChangeForOneTurn(self):
        acceleration = 0.0
        braking = 0.0
        
        # Total up all speed changes
        for car in self.Cars:
            braking += DRAG
            if not car.Engine is None:
                acceleration += car.Engine.GetSpeedChangeForOneTurn(self.Speed)
                braking += car.Engine.GetBrakingSpeed()
                
        
        # Apply speed and braking changes
        self.Speed += acceleration
        if self.Speed >= 0.0:
            if self.Speed > braking:
                self.Speed -= braking
            else:
                self.Speed = 0.0
        else:
            braking *= -1.0
            if (self.Speed < braking):
                self.Speed -= braking
            else:
                self.Speed = 0.0 
                
        self.Speed = round(self.Speed, 2)
        
    # Returns the coordinates of the square this would LIKE to move to, if feasible.
    # If it is not moving, it returns NONE.
    def CalculateMoveLocation(self, map, isForwardNotBack):
        if isForwardNotBack:
            return self.GetNextForwardTile(map)
        else:
            return self.GetNextBackwardTile(map)        
        
    def Move(self, map, isForwardNotBack):    
        if isForwardNotBack:
            self.MoveForward(map)
        else:
            self.MoveBackward(map)

    def GetNextForwardTile(self, map):
        frontCar = self.GetFrontCar()       
        currentTile = map[frontCar.X][frontCar.Y]
        offsetX, offsetY, newDirection, success = currentTile.GetNextTileOffset(
            map,
            frontCar.X,
            frontCar.Y,
            frontCar.Direction
        )
        return (self.GetFrontCar().X + offsetX,
            self.GetFrontCar().Y + offsetY,
            newDirection,
            success
        )
        
        
    def MoveForward(self, map):
        newX, newY, newDirection, success = self.GetNextForwardTile(map)
        
        # if a bad movement was returned, don't do anything
        if (success != Map.MapTile.NEXT_TILE_OFFSET_VALID):
            return
        
        #print newX, newY, newDirection
        #newX = self.GetFrontCar().X + offsetX
        #newY = self.GetFrontCar().Y + offsetY
        
        # Move each car
        for car in self.Cars:
            tempX, tempY, tempD = car.X, car.Y, car.Direction
            car.X, car.Y, car.Direction = newX, newY, newDirection
            newX, newY, newDirection = tempX, tempY, tempD
        
        return
        

    def GetNextBackwardTile(self, map):
        backCar = self.GetBackCar()
        currentTile = map[backCar.X][backCar.Y]
        offsetX, offsetY, newDirection, success = currentTile.GetNextTileOffset(
            map,
            backCar.X,
            backCar.Y,
            Utilities.ReverseDirection(backCar.Direction)
        )
        return (self.GetBackCar().X + offsetX,
            self.GetBackCar().Y + offsetY,
            newDirection,
            success
        )
        
    def MoveBackward(self, map):
        newX, newY, newDirection, success = self.GetNextBackwardTile(map)
        
        # If a bad movement was returned, don't do anything
        if (success != Map.MapTile.NEXT_TILE_OFFSET_VALID):
            return
        
        #print newX, newY, newDirection
        #newX = self.GetBackCar().X + offsetX
        #newY = self.GetBackCar().Y + offsetY
        
        newDirection = Utilities.ReverseDirection(newDirection)
        
        # Move each car
        reverseCars = list(self.Cars)
        reverseCars.reverse()
        for car in reverseCars:
            tempX, tempY, tempD = car.X, car.Y, car.Direction
            car.X, car.Y, car.Direction = newX, newY, newDirection
            newX, newY, newDirection = tempX, tempY, tempD
        
        return
    
# Represents a single TrainCar, with all the properties of that train car
# Note: It does store its own location and direction on the map, because otherwise the parent
# train object would need to store the location of each.
class TrainCar:
    def __init__(self, name, displayChar, displayColor, x, y, direction, engine):
        self.Name = name
        self.DisplayChar = displayChar
        self.DisplayColor = displayColor
        self.X = x
        self.Y = y
        
        # Direction refers to which way the FrontCoupler (if one exists) is pointing to
        self.Direction = direction
        
        # Rules by which this car can affect the increase/decrease of speed of the car
        self.Engine = engine
        
        self.ParentTrain = None
        
        # Which Player/Entity ownes this car. Also used for background shading of the car.
        self.Owner = None
        
        

    