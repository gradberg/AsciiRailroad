import Map
import Train
import Utilities
        
# Represents the state of the game, storing all active game information
class GameState:
    def __init__(self):
        self.Turn = 0
        self.Map = None
        self.Trains = []
        self.Player = None
        
    def AppendTrain(self, train):
        self.Trains.append(train)    

    # Code file responsible for doing a turn.
    def DoTurn(self):
        # Change speeds
        for train in self.Trains:
            if (train.HasCrashed == True):
                continue
        
            train.DoSpeedChangeForOneTurn()
            
        # ---- Move People (including Player?)
        
        movementTurns = self.CreateMovementTurns()
 
        # Move things
        for movementTurn in movementTurns:
            for train in movementTurn.Trains:
                if (train.HasCrashed == True):
                    train.Speed = 0
                    continue
                    
                if (train.HasCollided == True):
                    continue
            
                isForwardNotBack = True
                if (train.Speed < 0.0):
                    isForwardNotBack = False
                    
                # Determine if the attempt movement will.. cause problems.
                newX, newY, _, success = train.CalculateMoveLocation(self.Map, isForwardNotBack)
                
                if (success == Map.MapTile.NEXT_TILE_OFFSET_BAD_SWITCH
                    or success == Map.MapTile.NEXT_TILE_OFFSET_END_OF_LINE):
                    
                    train.HasCrashed = True
                    continue
                    
                # ---- Okay, its not moving off the tracks or into a bad switch. How about
                # Is it moving into another train and connecting?
                collidingTrain = self.CheckForCollision(train, newX, newY)                
                
                # If not hitting anything, just move the train and continue
                if (collidingTrain is None):    
                    train.Move(self.Map, isForwardNotBack)
                    continue
                    
                #print "Collision! ", self.Turn
                    
                # If the train this is trying to connect to has already crashed, 
                # attempting to combine with it will crash as well.
                # ---- This will eventually be changed, with 'crash' existing at the
                #      car level, not the train level.
                if (collidingTrain.HasCrashed == True):
                    train.HasCrashed = True
                    continue
                    
                # ---- Determine speed moving towards each other. Going too fast will cause a crash.
                    
                # Hitting something                    
                newTrain = self.MergeTrains(train, collidingTrain)
                if (not newTrain is None):
                    newTrain.Speed = 0.0
                    newTrain.HasCollided = True                    
                else:
                    # This is bad. They couldn't merge, which means they likely crashed into the 
                    # middle of each other...
                    train.HasCrashed = True
                    collidingTrain.HasCrashed = True
                
        # Clear any temporary state? (Like collision flags?)
        for train in self.Trains:
            train.HasCollided = False
                
        self.Turn += 1
     
    # stores all trains that will move this movement turn.
    class MovementTurn:
        def __init__(self, turnNumber):
            self.TurnNumber = turnNumber
            self.Trains = []
     
    # Returns a list of queues, each queue being one turn's movement.
    def CreateMovementTurns(self):
        result = [] # list of MovementTurn objects
        
        turnNumber = 0
        while (True):
            hadTrainWithMovement = False
            movementTurn = GameState.MovementTurn(turnNumber)
            
            for train in self.Trains:                
                #isForwardNotBack = True
                speed = train.Speed
                if (speed < 0.0):
                    #isForwardNotBack = False
                    speed *= -1                
                speed = int(round(speed, 0))
                
                if (speed >= turnNumber + 1):
                    movementTurn.Trains.append(train)
                    hadTrainWithMovement = True
            
            if (hadTrainWithMovement == False):
                break
                
            result.append(movementTurn)
            turnNumber += 1
        
        return result
    
    def CheckForCollision(self, currentTrain, newX, newY):
        collidingTrain = None
        for train in self.Trains:
            if (train is currentTrain):
                continue
            
            for car in train.Cars:
                if (car.X == newX and car.Y == newY):
                    
                    collidingTrain = train
                    break
                    
            if (not collidingTrain is None):
                break
                
        if (collidingTrain is None):
            # Not colliding with this train
            return None
            
        # ---- Check if it is a GOOD collision, or BAD collision, and return that?
        
        return collidingTrain
        
    def CheckForCollisions(map, trains, currentTrain):
        # Only check the front or the back depending on if the train is moving forward or backwards.
        isMovingForward = True
        currentCar = currentTrain.Cars[0]
        if (currentTrain.Speed == 0.0): return False
        
        if (currentTrain.Speed < 0.0): 
            isMovingForward = False
            lastCarIndex = len(currentTrain.Cars) - 1
            currentCar = currentTrain.Cars[lastCarIndex]
            
        atDamagingSpeed = currentTrain.Speed > 1.0 or currentTrain.Speed < -1.0
        atCrashSpeed = currentTrain.Speed > 2.0 or currentTrain.Speed < -2.0
        
        intersectingTrain, intersectingCar = None, None
        for train in trains:
            if (train is currentTrain): continue
            
            for car in train.Cars:
                if (car.X == currentCar.X and car.Y == currentCar.Y):
                    intersectingTrain = train
                    intersectingCar = car
                    break
            
            if (not intersectingTrain is None): break
           
        # No trains collided. Don't bother continuing.
        if (intersectingTrain is None): return False
            
        # There IS a collision. 
        isCrash = False
        canConnect = False
        
        # If the collided car does not match the front or back, then that means this train smacked 
        # into the middle of another train (probably at a + crossing). Thats an outright crash.
        isInMiddleOfTrain = not (intersectingTrain.GetFrontCar() is intersectingCar or 
            intersectingTrain.GetBackCar() is intersectingCar
        )    
        isCorrectAlignment = utilities.CanDirectionsConnect(currentCar.Direction, intersectingCar.Direction)
        
        #totalSpeed = 
        
        # ---- Need to make it real easy to split and combine trains
        #   ---- Remove any references TO trains from anything but train cars.
        #   ---- Convert the trains list to a proper object so that it has the function to split/combine trains
        # ---- Need easy functions to move cars around as necessary (for when one gets hit in the middle and,
        #      after the train object is split in two, the hit car is slid out of the way)
        # ---- Also need to preview the move of the train instead of moving it and figuring out the effect 
        #      afterwards. This is because it will be very difficult to move a train into another train, and 
        #      THEN figure out where the cars end up afterwards. It'll be alot easier to figure out
        #      if Collisions and such occur first, and then modify any train locations and speeds appropriately.
        
        if (isInMiddleOfTrain or not isCorrectAlignment):
            isCrash = True
        
        # If it did hit the correct end of the train, make sure the cars are appropriately aligned
        # so that they can merge. If not, its a crash    
        
        
        else:
            pass
        
        
        # Even if everything ele is correctly aligned, the speed of both trains, if too high, will
        # result in a crash.
        
        
        # Merge
        # ---- Set both trains as collided
        # ---- remove all cars from the other train and add them to his one
        # ---- re-aligned all cars to point in the right directon?
        
        
        return False
    
    # Splits a train into two trains (either because a car was decoupled, or it was speared in half...)
    def SplitTrainAfterCar(self, train, carIndex):
        # If the index is out of bounds, then fake split the train  
        if (carIndex < 0):
            return None, train
            
        if (carIndex >= len(train.Cars)):
            return train, None
        
        
        carsToTransfer = []
        for index in range(carIndex+1, len(train.Cars)):
            carsToTransfer.append(train.Cars[index])

        # Remove the first car BEFORE using it to create a
        # new train, because otherwise removing the car
        # afterwards will clear out its ParentTrain property
        train.RemoveCar(carsToTransfer[0])

        rearTrain = Train.Train(carsToTransfer[0])
        rearTrain.Speed = train.Speed
        rearTrain.HasCollided = train.HasCollided
        self.AppendTrain(rearTrain)        
        
        carsToTransfer.remove(carsToTransfer[0])        
        
        for car in carsToTransfer:
            # Remove FIRST, so that the ParentTrain property gets set right.
            train.RemoveCar(car)
            rearTrain.AppendCar(car)

        return train, rearTrain
        
    # This attempts to merge two trains. 
    # If it is successful, it returns the new train object (usually the 'front' train's existing
    #   object). If it fails, it returns None.
    def MergeTrains(self, train1, train2):
        car1, car2 = self.CanTrainsMerge(train1, train2)
        if (car1 is None):
            return None
        
        # Determine which end of each train gets merged
        addCarsToBeginning = train1.GetFrontCar() is car1
        takeCarsFromBeginning = train2.GetFrontCar() is car2
        
        # ---- Determine new total speed
        
        # move cars from train 2 to train 1
        while len(train2.Cars) > 0:
            carToTake = None
            if (takeCarsFromBeginning == True):
                carToTake = train2.GetFrontCar()
            else:
                carToTake = train2.GetBackCar()
            train2.RemoveCar(carToTake)
            
            if (addCarsToBeginning == True):
                train1.PrefixCar(carToTake)
            else:
                train1.AppendCar(carToTake)
                
        self.Trains.remove(train2)
        return train1
    
    # This checks if two trains can be merged.
    # If not, then it returns a None tuple. If it can, it returns the car on each
    # train that are adjacent and would merge.
    def CanTrainsMerge(self, train1, train2):    
        # First check that front/back cars of the trains are even adjacent. If not, its not going to happen
        frontCar1, backCar1 = train1.GetFrontCar(), train1.GetBackCar()
        frontCar2, backCar2 = train2.GetFrontCar(), train2.GetBackCar()
                
        if AreCarsAdjacent(frontCar1, frontCar2):
            if AreCarsCorrectlyOriented(
                frontCar1, 
                frontCar1.Direction, 
                frontCar2, 
                frontCar2.Direction):
                return frontCar1, frontCar2
            
        if AreCarsAdjacent(frontCar1, backCar2):
            if AreCarsCorrectlyOriented(
                frontCar1, 
                frontCar1.Direction,
                backCar2,
                Utilities.ReverseDirection(backCar2.Direction)):
                return frontCar1, backCar2
            
        if AreCarsAdjacent(backCar1, frontCar2):
            if AreCarsCorrectlyOriented(
                backCar1, 
                Utilities.ReverseDirection(backCar1.Direction),
                frontCar2,
                frontCar2.Direction):
                return backCar1, frontCar2
            
        if AreCarsAdjacent(backCar1, backCar2):
            if AreCarsCorrectlyOriented(
                backCar1, 
                Utilities.ReverseDirection(backCar1.Direction),
                backCar2,
                Utilities.ReverseDirection(backCar2.Direction)):
                return backCar1, backCar2
                
        return None, None
        
def AreCarsAdjacent(car1, car2):
    xDiff = car1.X - car2.X
    yDiff = car1.Y - car2.Y
    
    if (xDiff == 0 and yDiff == 0): return False
    if (xDiff > 1 or xDiff < -1): return False
    if (yDiff > 1 or yDiff < -1): return False
    return True        
    
def AreCarsCorrectlyOriented(car1, car1Direction, car2, car2Direction):
    x1,y1 = Utilities.GetOffsetsForDirection(car1Direction)    
    car1PointsAtCar2 = (
        ((car2.X - car1.X == x1) and (car2.Y - car1.Y == y1)) 
    )
    x1,y1 = Utilities.GetOffsetsForDirection(car2Direction)   
    car2PointsAtCar1 = (
        ((car1.X - car2.X == x1) and (car1.Y - car2.Y == y1)) 
    )
    
    return (CarInValidDirection(car1, car1Direction, car2) 
        and CarInValidDirection(car2, car2Direction, car1)
        and (car1PointsAtCar2 or car2PointsAtCar1)
    )
    
def CarInValidDirection(carA, carADirection, carB):
    offsets1 = Utilities.ReturnValidOffsetsForDirection(carADirection)
    
    xDiff = carB.X - carA.X
    yDiff = carB.Y - carA.Y
        
    if (OffsetsContain(offsets1, xDiff, yDiff)): return True
    return False
    
def OffsetsContain(offsets, x, y):
    for oX, oY in offsets:
        if (x == oX and y == oY): 
            return True        
    return False
    