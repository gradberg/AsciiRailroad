   
def ReverseDirection(direction):
    if direction == 'N': return 'S'
    if direction == 'NE': return 'SW'
    if direction == 'E': return 'W'
    if direction == 'SE': return 'NW'
    if direction == 'S': return 'N'
    if direction == 'SW': return 'NE'
    if direction == 'W': return 'E'
    if direction == 'NW': return 'SE'
    return 'X'
    

def GetOffsetsForDirection(direction):
    if direction == 'N':  return  0, -1
    if direction == 'NE': return  1, -1
    if direction == 'E':  return  1,  0
    if direction == 'SE': return  1,  1
    if direction == 'S':  return  0,  1
    if direction == 'SW': return -1,  1
    if direction == 'W':  return -1,  0
    if direction == 'NW': return -1, -1
    return 0,0
    
# ---- Convert these into a more generic rotation function?
def GetEastFromDirection(direction):
    if direction == 'N': return 'E'
    if direction == 'NE': return 'SE'
    if direction == 'E': return 'S'
    if direction == 'SE': return 'SW'
    if direction == 'S': return 'W'
    if direction == 'SW': return 'NW'
    if direction == 'W': return 'N'
    if direction == 'NW': return 'NE'
    return 'X'
def GetWestFromDirection(direction):
    if direction == 'N': return 'W'
    if direction == 'NE': return 'NW'
    if direction == 'E': return 'N'
    if direction == 'SE': return 'NE'
    if direction == 'S': return 'E'
    if direction == 'SW': return 'SE'
    if direction == 'W': return 'S'
    if direction == 'NW': return 'SW'
    return 'X'
def Get45DegreesFromDirection(direction):
    if direction == 'N': return 'NE'
    if direction == 'NE': return 'E'
    if direction == 'E': return 'SE'
    if direction == 'SE': return 'S'
    if direction == 'S': return 'SW'
    if direction == 'SW': return 'W'
    if direction == 'W': return 'NW'
    if direction == 'NW': return 'N'
    return 'X'    
def Get315DegreesFromDirection(direction):
    if direction == 'N': return 'NW'
    if direction == 'NE': return 'N'
    if direction == 'E': return 'NE'
    if direction == 'SE': return 'E'
    if direction == 'S': return 'SE'
    if direction == 'SW': return 'S'
    if direction == 'W': return 'SW'
    if direction == 'NW': return 'W'
    return 'X'
    
_offsetDirections = [
    ( 0, -1, ), # N
    ( 1, -1), # NE
    ( 1,  0), # E
    ( 1,  1), # SE
    ( 0,  1), # S
    (-1,  1), # SW
    (-1,  0), # W
    (-1, -1)  # NW
]
    
def ReturnValidOffsetsForDirection(direction):
    num = ConvertDirectionToNumber(direction)
    numCCW = num - 1
    if (numCCW < 0): numCCW += 8
    numCW = num + 1
    if (numCW > 7): numCW -= 8
    
    return [_offsetDirections[numCCW], _offsetDirections[num], _offsetDirections[numCW]]
    
    
def ConvertDirectionToNumber(direction):
    if direction == 'N': return 0
    if direction == 'NE': return 1
    if direction == 'E': return 2
    if direction == 'SE': return 3
    if direction == 'S': return 4
    if direction == 'SW': return 5
    if direction == 'W': return 6
    if direction == 'NW': return 7
    return 9999

# Determine if two directions represent car orientations that can be connected
def CanDirectionsConnect(direction1, direction2):
    n1 = ConvertDirectionToNumber(direction1)
    n2 = ConvertDirectionToNumber(direction2)
    
    diff = n1 - n2
    # N - N = 0, N - NE = -1, N - NW = -7.
    # N - S = -4, N - SE = -3, N - SW = -5.
    # +/- 2 and +/- 6 cannot connect
    
    # SW - SW = 0, SW - W = -1, SW - S = 1
    # SW - NE = 4, SW - N = 5, SW - E = 3
    
    if (diff == 2 or diff == -2 or diff == 6 or diff == -6):
        return False
    else:
        return True

# Takes a new direction, and makes sure it points 'front' compared to the current direction
# This is used so that all cars on a train always point forward (no mixtures of forwards 
# and backwards)
def NormalizeDirection(currentDirection, newDirection):
    nc = ConvertDirectionToNumber(currentDirection)
    nn = ConvertDirectionToNumber(newDirection)
    
    diff = nc - nn
    if (diff < 0):
        diff += 8
    
    if ((diff >= 0 and diff <= 1) or diff >= 7): # 45 Degree angles, just fine
        return newDirection
    elif (diff == 2 or diff == 6): # 90 and 180 angles, invalid
        return 'X'
    else:
        return ReverseDirection(newDirection)
