CAR_BRAKES = 0.1
class CarWithBrakes():
    def __init__(self):
        self.brakesOn = False
        
    def GetSpeedChangeForOneTurn(self, currentSpeed):
        # Does not provide any speed boost
        return 0.0
        
    def GetBrakingSpeed(self):
        if (self.brakesOn == True):
            return CAR_BRAKES
        else:
            return 0.0           
    
    def Activate(self):
        self.brakesOn = not self.brakesOn
        return True

# These are just speed; They should be power, which takes into account
# Car weights and such
MAX_SPEED = 3.0
ACCEL = 0.2
BRAKE = 0.3

# Placeholder engine that allows temporary development 
class FakeEngine:
    def __init__(self):
        self.brakePercentage = 0.0 # 0.0 to 1.0
        self.throttlePercentage = 0.3 # -1.0 to 1.0
       
    # ---- eventually will pass stuff in
    def GetSpeedChangeForOneTurn(self, currentSpeed):
        desiredMaxSpeed = round(MAX_SPEED * self.throttlePercentage, 2)
        acceleration = desiredMaxSpeed - currentSpeed
        
        if acceleration >= 0:
            if (acceleration > ACCEL):
                acceleration = ACCEL
            
        else:
            if (acceleration < -ACCEL):
                acceleration = -ACCEL
                                
        return acceleration
            
    def GetBrakingSpeed(self):
        return round(BRAKE * self.brakePercentage, 2)    
          
    def SetBrakes(self, percentage):
        if percentage < 0.0: percentage = 0.0
        if percentage > 1.0: percentage = 1.0
        self.brakePercentage = round(percentage, 2)

    def SetThrottle(self, percentage):
        if (percentage < -1.0): percentage = -1.0
        if (percentage >  1.0): percentage =  1.0
        self.throttlePercentage = round(percentage,2)
        
    def Activate(self):
        return False # Locomotives cannot be activated
    