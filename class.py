class bodypart:
    def __init__(self, name, dismembered, damageLoss):
            self.name = name
            self.dismembered = dismembered
            self.damageLoss = damageLoss


    def remove(self, dismembered, damageLoss):
        self.dismembered = True


leftHand = 'left hand', False, -10
rightHand = 'right hand', False, -10
leftArm = 'left arm', False, -22
rightArm = 'right arm', False, -22
leftFoot = 'left foot', False, -10
rightFoot = 'right foot', False, -10
leftLeg = 'left leg', False, -28
rightLeg = 'right leg', False, -28
