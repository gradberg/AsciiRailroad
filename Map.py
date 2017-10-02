
import libtcodpy as libtcod
import Utilities

WIDTH = 160
HEIGHT = 45

class TrackSwitch:
    def __init__(self, switchTile, primaryTile, primaryDirection, secondaryTile, secondaryDirection):
        self.SwitchTile = switchTile
        self.PrimaryTile = primaryTile
        self.PrimaryDirection = primaryDirection
        self.SecondaryTile = secondaryTile
        self.SecondaryDirection = secondaryDirection
        self.IsSwitched = False
        self.ControlTile = None
        
    def Activate(self):
        # ---- Do not switch if a train has cars on both the switch tile and the primary/secondary
        self.IsSwitched = not self.IsSwitched
        if (not self.ControlTile is None):
            self.ControlTile.trackChar = '>'
            if (self.IsSwitched):
                self.ControlTile.trackChar = '<'

class MapLocation:
    def __init__(self, name):
        self.Name = name
        self.Tiles = []        
        
    def AssignTile(self, mapTile):
        self.Tiles.append(mapTile)
        mapTile.Location = self        
                
class MapTile:
    def __init__(self, trackChar):
        self.trackChar = trackChar
        
        # Indicates if this tile connects to surrounding tiles.
        self.IsTrack = False
        self.N = False        
        self.NE = False
        self.E = False
        self.SE = False
        self.S = False
        self.SW = False
        self.W = False
        self.NW = False
        
        # Indicates this tile is part of a switch          
        self.Switch = None
        self.IsSwitchControl = False 
        
        # Indicates this tile is part of a defined building/map location
        self.Location = None
        
    def CountConnections(self):
        result = 0
        if (self.N == True): result += 1
        if (self.NE == True): result += 1
        if (self.E == True): result += 1
        if (self.SE == True): result += 1
        if (self.S == True): result += 1
        if (self.SW == True): result += 1
        if (self.W == True): result += 1
        if (self.NW == True): result += 1
        return result
        
    def FindAdjacentConnections(self):
        if self.N and self.NE:
            return 'N', 'NE'
        if self.NE and self.E:
            return 'NE','E'
        if self.E and self.SE:
            return 'E','SE'
        if self.SE and self.S:
            return 'SE','S'
        if self.S and self.SW:
            return 'S','SW'
        if self.SW and self.W:
            return 'SW','W'
        if self.W and self.NW:
            return 'W','NW'
        if self.NW and self.N:
            return 'NW','N'
        return 'X','X'
        
    def IsConnected(self, direction):
        if (direction == 'N' and self.N): return True
        if (direction == 'NE' and self.NE): return True
        if (direction == 'E' and self.E): return True
        if (direction == 'SE' and self.SE): return True
        if (direction == 'S' and self.S): return True
        if (direction == 'SW' and self.SW): return True
        if (direction == 'W' and self.W): return True
        if (direction == 'NW' and self.NW): return True
        return False
        
    # Enumerations for valid Next tile offsets
    NEXT_TILE_OFFSET_VALID = 0
    NEXT_TILE_OFFSET_END_OF_LINE = 1
    NEXT_TILE_OFFSET_BAD_SWITCH = 2
        
    def GetNextTileOffset(self, map, x, y, direction):
        # Use the normal logic to get the next tile
        normalDirection = self.GetNextMoveDirection(direction)
        normalOffsetX, normalOffsetY = Utilities.GetOffsetsForDirection(normalDirection)
        normalTile = map.Tile(x + normalOffsetX,y + normalOffsetY)
            
        # Could not get a valid direction to move to, which means there is no more track
        # in this direction
        if (normalDirection == 'X'):
            return 0,0,'X', self.NEXT_TILE_OFFSET_END_OF_LINE
        
        # If this is not on a switch, or if the movement isn't through the switch,
        # just return that value.
        if (self.Switch is None):
            return normalOffsetX, normalOffsetY, normalDirection, self.NEXT_TILE_OFFSET_VALID
            
        movingOnSwitch = (self.Switch.SwitchTile is normalTile or
            self.Switch.PrimaryTile is normalTile or
            self.Switch.SecondaryTile is normalTile)
        
        if (movingOnSwitch == False):
            return normalOffsetX, normalOffsetY, normalDirection, self.NEXT_TILE_OFFSET_VALID
            
        # If movement is onto the switch tile, only allow it if the switch is in the correct position
        if (self.Switch.SwitchTile is normalTile):
            isAllowed = ((self.Switch.PrimaryTile is self and self.Switch.IsSwitched == False) or
                (self.Switch.SecondaryTile is self and self.Switch.IsSwitched == True))
                
            if (isAllowed):
                return normalOffsetX, normalOffsetY, normalDirection, self.NEXT_TILE_OFFSET_VALID
            else:
                return 0,0,'X', self.NEXT_TILE_OFFSET_BAD_SWITCH
        
        # Otherwise movement must be on to either the primary or secondary tile. Pick the correct
        # one based on the isSwiched setting.
        normalDirection = self.Switch.PrimaryDirection
        if (self.Switch.IsSwitched):
            normalDirection = self.Switch.SecondaryDirection
            
        normalOffsetX, normalOffsetY = Utilities.GetOffsetsForDirection(normalDirection)
        
        return normalOffsetX, normalOffsetY, normalDirection, self.NEXT_TILE_OFFSET_VALID
    
    def GetNextMoveDirection(self, direction):
        if direction == 'N':
            if self.N:  return 'N'        
            if self.NE: return 'NE'       
            if self.NW: return 'NW'
            
        if direction == 'NE':
            if self.NE: return 'NE'        
            if self.N:  return 'N'       
            if self.E:  return 'E'
            
        if direction == 'E':
            if self.E:  return 'E'        
            if self.NE: return 'NE'       
            if self.SE: return 'SE'
        
        if direction == 'SE':
            if self.SE: return 'SE'        
            if self.E:  return 'E'       
            if self.S:  return 'S'
        
        if direction == 'S':
            if self.S:  return 'S'        
            if self.SE: return 'SE'       
            if self.SW: return 'SW'
        
        if direction == 'SW':
            if self.SW: return 'SW'        
            if self.S:  return 'S'       
            if self.W:  return 'W'
      
        if direction == 'W':
            if self.W:  return 'W'        
            if self.SW: return 'SW'       
            if self.NW: return 'NW'
        
        if direction == 'NW':
            if self.NW: return 'NW'       
            if self.W:  return 'W'       
            if self.N:  return 'N'
        
        # ---- this likely indicates that its the end of the line or something. This would probably equate to a crash.
        return 'X'    # won't go anywhere. Should log assertion failure.
            

# Helper class to draw track on the screen        
class TrackPlotter:
    def __init__(self, map, x, y, firstPlotChar):
        self.map = map
        self.x = x
        self.y = y
        self.firstPlot = True
        self.firstPlotChar = firstPlotChar
        
        # MapLocation for which all current ploted points will be assigned to.
        self.CurrentLocation = None
        
    # Repositions the current point, which is useful for creating switches...    
    def SetTo(self, x, y):
        self.x = x
        self.y = y
        
    def PlotTo(self, xTo, yTo):
        # Plot the start point as directly pointing to the new location.
        # At the moment this will use the Line Algorithm provided in that one thingy.
        
        # If this is the very start of the plot, put a 'star' indicating that its the end
        # of a track.        
        if (self.firstPlot == True):
            self.map.Tile(self.x,self.y).trackChar = self.firstPlotChar
            self.map.Tile(self.x,self.y).IsTrack = True            
            if (not self.CurrentLocation is None):
                self.CurrentLocation.AssignTile(self.map.Tile(self.x,self.y))                
            self.firstPlot = False
        
        libtcod.line_init(self.x, self.y, xTo, yTo)
        x,y = libtcod.line_step()
        while (not x is None):
            # ---- Determine the direction between this track and the last.
            xd = x - self.x
            yd = y - self.y
            
            newTile = self.map.Tile(x,y)
            oldTile = self.map.Tile(self.x, self.y)            
            if (xd == 0 and yd == -1): # going north
                newTile.trackChar = '|'
                newTile.S = True
                newTile.IsTrack = True
                oldTile.N = True
            if (xd == 1 and yd == -1): # going northeast
                newTile.trackChar = '/'
                newTile.SW = True
                newTile.IsTrack = True
                oldTile.NE = True
            if (xd == 1 and yd == 0): # going east
                newTile.trackChar = '-'
                newTile.W = True
                newTile.IsTrack = True
                oldTile.E = True
            if (xd == 1 and yd == 1): # going southeast
                newTile.trackChar = '\\'
                newTile.NW = True
                newTile.IsTrack = True
                oldTile.SE = True
            if (xd == 0 and yd == 1): # going south
                newTile.trackChar = '|'
                newTile.N = True
                newTile.IsTrack = True
                oldTile.S = True
            if (xd == -1 and yd == 1): # going southwest
                newTile.trackChar = '/'
                newTile.NE = True
                newTile.IsTrack = True
                oldTile.SW = True
            if (xd == -1 and yd == 0): # going west
                newTile.trackChar = '-'
                newTile.E = True
                newTile.IsTrack = True
                oldTile.W = True
            if (xd == -1 and yd == -1): # going northwest
                newTile.trackChar = '\\'
                newTile.SE = True
                newTile.IsTrack = True
                oldTile.NW = True
                
            # If either the old or new location has more than 2 connections, then it is a switch. Mark it as such.
            if newTile.CountConnections() == 3 and newTile.Switch is None:
                self.MakeSwitchAt(x, y)
                
            if oldTile.CountConnections() == 3 and oldTile.Switch is None:            
                self.MakeSwitchAt(self.x, self.y)
                
            # If this is on a current location, then assign it to that location            
            if (not self.CurrentLocation is None):
                self.CurrentLocation.AssignTile(newTile)            
                
            # Move along, using the member variables to store the previous location.
            self.x = x
            self.y = y
            x,y = libtcod.line_step()
            
        self.x = xTo
        self.y = yTo
        
    def MakeSwitchAt(self, x, y):
        switchTile = self.map.Tile(x,y)
        
        d1,d2 = switchTile.FindAdjacentConnections()
        
        rd1 = Utilities.ReverseDirection(d1)
        rd2 = Utilities.ReverseDirection(d2)
        
        primaryDirection = None
        secondaryDirection = None
        if (switchTile.IsConnected(rd1) == True):
            primaryDirection = d1
            secondaryDirection = d2
        if (switchTile.IsConnected(rd2) == True):
            primaryDirection = d2
            secondaryDirection = d1
        
        # If this cannot determine the primary direction, then don't create the switch.
        if (primaryDirection is None): return
        
        # That one is the primary, the other is the secondary.
        primaryOffsetX, primaryOffsetY = Utilities.GetOffsetsForDirection(primaryDirection)
        primaryTile = self.map.Tile(x + primaryOffsetX,y + primaryOffsetY)
                
        secondaryOffsetX, secondaryOffsetY = Utilities.GetOffsetsForDirection(secondaryDirection)
        secondaryTile = self.map.Tile(x + secondaryOffsetX,y + secondaryOffsetY)
               
        switch = TrackSwitch(switchTile, primaryTile, primaryDirection, secondaryTile, secondaryDirection)        
        switchTile.Switch = switch
        primaryTile.Switch = switch
        secondaryTile.Switch = switch
        
        # ---- Find the nearest open tile to create the manual switch activator at?
        controlDirection = Utilities.GetEastFromDirection(primaryDirection)
        controlOffsetX, controlOffsetY = Utilities.GetOffsetsForDirection(controlDirection)
        controlX = x + controlOffsetX
        controlY = y + controlOffsetY
        
        controlTile = self.map.Tile(controlX,controlY)
        if (controlTile.IsTrack == True or controlTile.IsSwitchControl == True): return
        
        controlTile.IsSwitchControl = True
        controlTile.trackChar = '>'
        controlTile.Switch = switch
        switch.ControlTile = controlTile
        
class Map:
    def __init__(self):
        self.Locations = []        
        self.MapArray = [[ MapTile(' ') 
            for y in range(HEIGHT) ] 
                for x in range(WIDTH) ]
        
    def Tile(self, x, y):
        return self.MapArray[x][y]
        
    def AddLocation(self, mapLocation):
        self.Locations.append(mapLocation)
        return mapLocation
                    
    def InitializeDevMap(self):                
        # Create locations on the map
        westYard = self.AddLocation(MapLocation("West Yard"))
        eastYard = self.AddLocation(MapLocation("East Yard"))        
    
        # Create the track    
        p = TrackPlotter(self, 5,10, '-')
        p.PlotTo(15,10)
        p.PlotTo(19,13)
        p.PlotTo(19,16)
        p.PlotTo(18,17)
        p.PlotTo(6 ,17)
        p.PlotTo(4 ,15)
        p.PlotTo(4 ,11)
        p.PlotTo(5,10)
        
        # Yard tracks
        p.CurrentLocation = westYard
        p.SetTo(18,17) 
        p.PlotTo(16,19) # track one
        p.PlotTo(7, 19)    
        
        p.SetTo(16,19) 
        p.PlotTo(14,21) # switch
        p.PlotTo(7, 21) # track two
        p.PlotTo(5,19)
        p.PlotTo(2,19)
        p.PlotTo(7,19)
        
        p.SetTo(14,21) 
        p.PlotTo(12,23) # switch
        p.PlotTo(4, 23) # track three
        
        p.SetTo(12,23)
        p.PlotTo(10,25) # switch
        p.PlotTo(4, 25) # track four
        p.CurrentLocation = None
        
        p.SetTo(2,19) # dumb bottom-left side track
        p.PlotTo(1,20)
        p.PlotTo(1,30)
        
        # Line off the right side
        p.SetTo(19,15)
        p.PlotTo(20,16)
        p.PlotTo(25, 18)
        p.PlotTo(60, 17)
        p.PlotTo(93, 19)
        p.PlotTo(130, 18)

        # Second Yard
        p.CurrentLocation = eastYard
        p.SetTo(65, 17)
        p.PlotTo(66, 18)
        p.PlotTo(66, 36)
            
        p.SetTo(66,22)
        p.PlotTo(67,23) # First Line
        p.PlotTo(78,23)
        
        p.SetTo(66,24)
        p.PlotTo(67,25) # Second Line
        p.PlotTo(78,25)
        
        p.SetTo(66,26)
        p.PlotTo(67,27) # Third Line
        p.PlotTo(77,27)
            
        p.SetTo(66, 28)
        p.PlotTo(67,29) # Fourth Line
        p.PlotTo(76,29)
        
        p.SetTo(66, 20)
        p.PlotTo(67, 19) # Triangluar connection to allow trains to flip around.
        p.PlotTo(70,19)
        p.PlotTo(71,18)
        
        # ---- Validate that no tracks have 90 degree turns unless they're cross tracks or switches.
        # ---- Validate that no tracks have more than 3 connections, and that two of those are adjacent.
