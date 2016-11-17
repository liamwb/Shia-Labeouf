class bodypart:
    def __init___(self, name, dismembered, damageLoss):
            self.name = name
            self.dismembered = dismembered
            self.damageLoss = damageLoss


    def remove(self, dismembered, damageLoss):
        self.dismembered = True


leftHand = bodypart()
leftHand = bodypart.name = ('left hand')
leftHand = bodypart.dismembered(False)
leftHand = bodypart.damageLoss(-5)

