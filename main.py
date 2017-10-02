import logging
import libtcodpy as libtcod
import Map as MOD_MAP
import player as MOD_PLAYER
import Train as MOD_TRAIN
import steamEngine as MOD_ENGINE
import screen as MOD_SCREEN

import GameState

def handleKeys(gameState):   
    key = libtcod.console_wait_for_keypress(False)
    
    if key.pressed == False:
        return False, 0
    
    if key.c == ord('Q'):
        return True, 0
        
    if key.c == ord(' '):
        return False, 1
    
    # ---- These need to be changed to only be usable if the player is on a car or location
    #      that they appply to.
    if key.c == ord('t'):
        if not gameState.Player.GetTrain() is None:
            engine = gameState.Player.OnCar.Engine
            engine.SetThrottle(engine.throttlePercentage + 0.1)
        return False, 0
    
    if key.c == ord('g'):
        if not gameState.Player.GetTrain() is None:
            engine = gameState.Player.OnCar.Engine
            engine.SetThrottle(engine.throttlePercentage - 0.1)
        return False, 0
    
    if key.c == ord('y'):
        if not gameState.Player.GetTrain() is None:
            engine = gameState.Player.OnCar.Engine
            engine.SetBrakes(engine.brakePercentage + 0.1)
        return False, 0
    
    if key.c == ord('h'):
        if not gameState.Player.GetTrain() is None:
            engine = gameState.Player.OnCar.Engine
            engine.SetBrakes(engine.brakePercentage - 0.1)
        return False, 0
        
    if key.c == ord('d'):
        return disconnectCar(gameState)
    
    if key.vk == libtcod.KEY_UP: # Up, or forward a car, or off the front of the train
        return movePlayer(gameState, 'N')
    if key.vk == libtcod.KEY_DOWN: # Down, or back a car, or off the back of the train
        return movePlayer(gameState, 'S')
    if key.vk == libtcod.KEY_LEFT: # Left, or off the left side of the car
        return movePlayer(gameState, 'W')
    if key.vk == libtcod.KEY_RIGHT: # Up, or off the right side of the car
        return movePlayer(gameState, 'E')
        
    if key.c == ord('a'):
        didMove = gameState.Player.Activate(gameState.Map)
        if (didMove):
            return False, 1
        else:
            return False, 0
        
    return False, 0
    
def movePlayer(gameState, direction):
    didMove = gameState.Player.Move(gameState.Map, gameState.Trains, direction)
    if didMove:
        return False, 1
    else:
        return False, 0    

def disconnectCar(gameState):
    if gameState.Player.GetTrain() is None:
        # does nothing on foot as of yet    
        return False, 0
        
    elif (gameState.Player.OnCar is gameState.Player.GetTrain().GetBackCar()):
        # does nothing if you're on the back car    
        return False, 0
    else:
        train = gameState.Player.GetTrain()
        carIndex = train.GetCarIndex(gameState.Player.OnCar)
        newTrain1, newTrain2 = gameState.SplitTrainAfterCar(train, carIndex)
        # Some sort of logging if it failed? 
        # Message of somew sort?
        return False, 1
    
# Initialize logging
logging.basicConfig(level=logging.DEBUG)    

# Console Initialization
#libtcod.console_set_custom_font('terminal12x12_gs_ro.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_ASCII_INROW)
#libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'Rogue Locomotive', False)
#libtcod.console_set_default_foreground(0, libtcod.white)
MOD_SCREEN.Initialize()


# Initial game
_gameState = GameState.GameState()
_gameState.Map = MOD_MAP.Map()
_gameState.Map.InitializeDevMap()

playerTrain = MOD_TRAIN.Train(MOD_TRAIN.TrainCar("Locomotive", 'L',libtcod.black,    13, 10, 'E', MOD_ENGINE.FakeEngine()))
playerTrain.AppendCar(MOD_TRAIN.TrainCar("Tender",  'T',libtcod.black,    12, 10, 'E', None))
#playerTrain.AppendCar(MOD_TRAIN.TrainCar("Boxcar",  'B',libtcod.dark_red, 11, 10, 'E', MOD_ENGINE.CarWithBrakes()))
#playerTrain.AppendCar(MOD_TRAIN.TrainCar("Boxcar",  'B',libtcod.dark_red, 10, 10, 'E', MOD_ENGINE.CarWithBrakes()))
#playerTrain.AppendCar(MOD_TRAIN.TrainCar("Flatcar", 'F',libtcod.sepia,     9, 10, 'E', MOD_ENGINE.CarWithBrakes()))
#playerTrain.AppendCar(MOD_TRAIN.TrainCar("Boxcar",  'B',libtcod.dark_red,  8, 10, 'E', MOD_ENGINE.CarWithBrakes()))
#playerTrain.AppendCar(MOD_TRAIN.TrainCar("Boxcar",  'B',libtcod.dark_red,  7, 10, 'E', MOD_ENGINE.CarWithBrakes()))
#playerTrain.AppendCar(MOD_TRAIN.TrainCar("Caboose", 'C',libtcod.red,      11, 10, 'E', MOD_ENGINE.CarWithBrakes()))
_gameState.AppendTrain(playerTrain)

_gameState.Player = MOD_PLAYER.Player(13,12, None, None)    

secondTrain = MOD_TRAIN.Train(MOD_TRAIN.TrainCar("Flatcar", 'F',libtcod.sepia, 5, 23, 'W', MOD_ENGINE.CarWithBrakes()))
secondTrain.AppendCar(MOD_TRAIN.TrainCar("Flatcar", 'F',libtcod.sepia, 6, 23, 'W', MOD_ENGINE.CarWithBrakes()))
secondTrain.AppendCar(MOD_TRAIN.TrainCar("Flatcar", 'F',libtcod.sepia, 7, 23, 'W', MOD_ENGINE.CarWithBrakes()))
secondTrain.Cars[0].Engine.Activate()
_gameState.AppendTrain(secondTrain)

thirdTrain = MOD_TRAIN.Train(
    MOD_TRAIN.TrainCar("Boxcar",  'B',libtcod.dark_red,  8, 25, 'E', MOD_ENGINE.CarWithBrakes())
    )
_gameState.AppendTrain(thirdTrain)

# Main game loop
while not libtcod.console_is_window_closed():
    MOD_SCREEN.DrawScreen(_gameState)
    exit, turns = handleKeys(_gameState)
    if exit:
        break
        
    for count in range(turns):
        _gameState.DoTurn()
        