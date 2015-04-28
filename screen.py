import libtcodpy as libtcod
import Map as MOD_MAP
import string

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

VISIBLE_MAP_WIDTH = SCREEN_WIDTH - 30 # Accounts for the GUI
VISIBLE_MAP_HEIGHT = SCREEN_HEIGHT

   
fmt = string.Formatter()

def Initialize():
    libtcod.console_set_custom_font('terminal12x12_gs_ro.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_ASCII_INROW)
    libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'Rogue Locomotive', False)
    libtcod.console_set_default_foreground(0, libtcod.white)


def DrawScreen(gameState):
    libtcod.console_clear(0)    
    
    # ---- Eventually this needs to take into account the window of view you have.
    # ---- Get the player's current location
    x,y = gameState.Player.GetLocation()
        
    # ---- Eventually take into account some theoretical maximum map size, but meh.
    
    
    # ---- Use the player's current location to determine the visible window.   
    visibleOffsetX = (VISIBLE_MAP_WIDTH/2)- x
    
    # the `- 10` makes the action take player higher to the top of the screen.
    visibleOffsetY = (VISIBLE_MAP_HEIGHT/2) - y - 10

    drawTiles(gameState.Map, visibleOffsetX, visibleOffsetY)
    drawTrains(gameState.Trains, gameState.Player, visibleOffsetX, visibleOffsetY)
    drawPlayers(gameState.Player, visibleOffsetX, visibleOffsetY)

    drawUi(gameState)
    
    libtcod.console_flush()
    
def drawTiles(map, xVisibleOffset, yVisibleOffset):
    for y in range(MOD_MAP.HEIGHT):
        for x in range(MOD_MAP.WIDTH):
            drawTile(map[x][y],x,y, xVisibleOffset, yVisibleOffset)
            
def drawTrains(trains, player, visibleOffsetX, visibleOffsetY):    
    playerTrain = player.GetTrain()
    for train in trains:
        isPlayerTrain = train is playerTrain
        for car in train.Cars:
            # Color train background based on the train's 'friendliness'
            # ---- Granted this might be more accurate to do based on CAR (and train)
            backgroundColor = libtcod.grey
            if (train.HasCrashed == True):
                backgroundColor = libtcod.light_red
            elif (isPlayerTrain == True):
                backgroundColor = libtcod.white
        
            drawCar(car, visibleOffsetX, visibleOffsetY, backgroundColor)
        
            #libtcod.console_put_char(0, car.X, car.Y, car.DisplayChar, libtcod.BKGND_NONE)
            #libtcod.console_set_char_foreground(0, car.X, car.Y, car.DisplayColor)
            
            # Color train background based on the train's 'friendliness'
            # ---- Granted this might be more accurate to do based on CAR (and train)
            #if (train.HasCrashed == True):
            #    libtcod.console_set_char_background(0, car.X, car.Y, libtcod.light_red, libtcod.BKGND_SET)
            #elif (isPlayerTrain == True):
            #    libtcod.console_set_char_background(0, car.X, car.Y, libtcod.white, libtcod.BKGND_SET)
            #else:
            #    libtcod.console_set_char_background(0, car.X, car.Y, libtcod.grey, libtcod.BKGND_SET)
            
def drawCar(car, visibleOffsetX, visibleOffsetY, backgroundColor):
    visible, screenX, screenY = getScreenCoordinates(car.X, car.Y, visibleOffsetX, visibleOffsetY)
    if (visible == False):
        # cannot see me :)
        return

    libtcod.console_put_char(0, screenX, screenY, car.DisplayChar, libtcod.BKGND_NONE)
    libtcod.console_set_char_foreground(0, screenX, screenY, car.DisplayColor)
    libtcod.console_set_char_background(0, screenX, screenY, backgroundColor, libtcod.BKGND_SET)


def drawPlayers(player, visibleOffsetX, visibleOffsetY):    
    playerX, playerY = player.GetLocation()
    visible, screenX, screenY = getScreenCoordinates(playerX, playerY, visibleOffsetX, visibleOffsetY)
    if (visible == False):
        # cannot see me :)
        return    
    
    libtcod.console_put_char(0, screenX, screenY, '@',libtcod.BKGND_NONE)
    libtcod.console_set_char_background(0, screenX, screenY, libtcod.black, libtcod.BKGND_SET)

def drawUi(gameState):    
    libtcod.console_print(0, 52, 2, fmt.format("Turn:     {0}", gameState.Turn))
    
    if gameState.Player.OnCar is None:
        # Display anything relevant on the ground
        tile = gameState.Map[gameState.Player.X][gameState.Player.Y]
        if (tile.IsSwitchControl == True):
            drawUiSwitch(tile.Switch)
        
    else:
        # Display based on the appropriate car
        carName = gameState.Player.OnCar.Name
        
        libtcod.console_print(0, 52, 4, gameState.Player.OnCar.Name)
        
        if (carName == "Locomotive"):
            drawUiLocomotive(gameState.Player)
        elif (carName == "Tender"):
            pass # Eventually display tender information?
        else:
            # Assuming all remaining cars have hand brakes
            drawUiNormalCar(gameState.Player)
        
        drawUiAnyCar(gameState.Player)

def drawUiSwitch(switch):
    libtcod.console_print(0, 52, 6, "(a) Activate Switch")
        
def drawUiLocomotive(player):
    libtcod.console_print(0, 52, 6, fmt.format("      Speed:    {0}", player.GetTrain().Speed))
    libtcod.console_print(0, 52, 7, fmt.format("(t)(g)Throttle: {0}", player.OnCar.Engine.throttlePercentage))
    libtcod.console_print(0, 52, 8, fmt.format("(y)(h)Brakes:   {0}", player.OnCar.Engine.brakePercentage))
    
def drawUiNormalCar(player):
    if (player.OnCar.Engine is None): return

    message = "Brakes are off"
    if (player.OnCar.Engine.brakesOn == True):
        message = "Brakes are *on*"
    libtcod.console_print(0, 52, 6, message)
    libtcod.console_print(0, 52, 7, "(a) Toggle Brakes")
    
def drawUiAnyCar(player):
    libtcod.console_print(0, 52, 12, "(up)(down)")    
    libtcod.console_print(0, 52, 13, "  Move one car")
    libtcod.console_print(0, 52, 14, "(left)(right)")
    libtcod.console_print(0, 52, 15, "  Jump off side of car")
    libtcod.console_print(0, 52, 16, "(d)")
    libtcod.console_print(0, 52, 17, "  Disconnect trailing cars")

def drawTile(tile, x, y, visibleOffsetX, visibleOffsetY):
    visible, screenX, screenY = getScreenCoordinates(x, y, visibleOffsetX, visibleOffsetY)
    if (visible == False):
        # cannot see me :)
        return

    background = libtcod.BKGND_NONE
    
    libtcod.console_put_char(0, screenX, screenY, tile.trackChar, libtcod.BKGND_NONE)
    if (not tile.Switch is None):
        color = libtcod.dark_sea
        
        if (tile.Switch.IsSwitched == False and tile.Switch.SecondaryTile is tile):
            color = libtcod.orange
        if (tile.Switch.IsSwitched == True  and tile.Switch.PrimaryTile is tile):
            color = libtcod.orange         
    
        libtcod.console_set_char_background(0, screenX, screenY, color, libtcod.BKGND_SET)
    elif (tile.IsTrack == True):
        libtcod.console_set_char_background(0, screenX, screenY, libtcod.darker_sepia, libtcod.BKGND_SET)
        
def getScreenCoordinates(x, y, visibleOffsetX, visibleOffsetY):
    # First get the screen X/Y coordinates (based on the player's location)
    screenX = x + visibleOffsetX
    screenY = y + visibleOffsetY
    hidden = (screenX < 0 or 
        screenX >= VISIBLE_MAP_WIDTH or 
        screenY < 0 or
        screenY >= VISIBLE_MAP_HEIGHT)
      
    return not hidden, screenX, screenY
    