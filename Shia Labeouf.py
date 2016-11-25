import sys
import random

print('Welcome to the Shia Labeouf experience. \nFor help type \'help\', or to begin type \'go!\'')

#what happens when you die
def death():
    print('You have died. In the morning, Shia will devour your body, \nBefore waiting in ravenous hunger to feast again.')
    sys.exit()

#A bit of text
def running_for_your_life():
    print('Running for your life \n(From Shia Labeouf)')
    print('He\'s brandishing a knife. \n(It\'s Shia Labeouf)')
    print('Lurking in the shadows')
    print('...')
    print('...')
    print('Hollywood superstar Shia Labeouf.')
    print('Living in the woods, \n(Shia Labeouf)')
    print('Killing for sport, \n(Shia Labeouf)')
    print('Eating all the bodies \nActual, cannibal Shia Labeouf.')
    print('----- \n-----')
    print('Now it\'s dark, and you seem to have lost him, \nBut your hopelessly lost yourself; \nStranded with a murderer...')
    print('------ \n------')

#a list of words that relate to shia
at_shia = ['him', 'shia', 'shia labeouf']
#a list of things people might use to go *to* something
to_list = ['to', 'towards', 'toward', 'at',]
#a list of things people might use to move *away* from something
away_list = ['away', 'from', 'back', 'out']
#a list of things people might say if they wanted to eat something
eat_list = ['gnaw', 'eat', 'chew', 'devour',]
#a list of things people might say to refer to something of theirs in the first person
self_list = ['my', 'mine',]
#things people might say if they wanted to stand up
up_list = ['stand', 'get up',]
#things people might say if they wanted to get a bear trap off them
off_trap_list = ['remove', 'get off', 'open', 'take off', 'pry', 'rip off',]
#things people might say if they wanted to attack something
fight_list = ['fight', 'attack', 'kill', 'hit',]
#list of things you would say to get in the cottage
cottage_list = ['inside', 'in',]


#organised as location : [ways you can go from there]
areas = {'woods1' : ['east'], 'dark woods' : ['west', 'south'], 'bear woods' : ['north', 'south'], 'cottage' : ['north', 'east'], 'winning woods':''}

def help_():
    print('Type \'look\' to look around at your surroundings.')
    print('Type \'walk to [a place]\' to walk there, or \'run\' to run there')
    print('Typing \'sneak to [a place]\' will have you slowly move there, without alerting enemies.')
    print('During a fight, type punch or kick to determine method of attack, \nfollowed by the bodypart you wish to target.')
    print('Kicks do more damage than punches, but you have a lower chance of landing them.')
    print('Typing \'go\' will begin your adventure!')

#a function that checks if the player is walking in a given direction (eg. to something)
#well actually it just checks all the words in a string to see if there is a matching word in a list
    #so i don't know why i called it check_direction, it should really have been check_match or something
def check_direction(list, string):
               string = string.split(' ')
               for item in string:
                   for i in list:
                       if item == i:
                           return True
               return False

#-------
#health values for fight one
shiaHealth = 350
playerHealth = 300

# The adjusted odds of things happening depending on how the player enters the cottage
#in order, the odds go: 1/2, 1/3, 1/4, 1/6, 1/10, 1/12, 2/3, 9/10
#	the adjusted lists follow (Using fractions of base 120 to generate probabilities)

snuckIn = [60, 40, 30, 20, 12, 10, 80, 108]
walkedIn = [90, 60, 45, 30, 18, 15, 120, 156]
ranIn = [75, 50, 38, 25, 15, 13, 100, 135]
gotSeen = [105, 70, 53, 35, 21, 18, 140, 189]

#just in case something goes wrong
theOdds = snuckIn

#body parts... you know, in case you lose some of them
class bodypart:
    def __init__(self, name, dismembered, damageLoss):
            self.name = name
            self.dismembered = dismembered
            self.damageLoss = damageLoss


    def dismember(self, damageLoss):
        global bodypartList
        global playerHealth
        if self.dismembered == True:
            print('You have managed to dismember the same article twice')
        else:
            self.dismembered = True
            bodypartList.remove(self.name)
            if 'arm' in self.name:
                #dismebering the hand attached to the arm in question
                if 'left' in self.name:
                    leftHand.dismembered = True
                    bodypartList.remove(leftHand.name)
                elif 'right' in self.name:
                    rightHand.dismembered = True
                    bodypartList.remove(rightHand.name)
            elif 'leg' in self.name:
                #dismebering the foot attached to the leg in question
                if 'left' in self.name:
                    leftFoot.dismembered = True
                    bodypartList.remove(leftFoot.name)
                elif 'right' in self.name:
                    rightFoot.dismembered = True
                    bodypartList.remove(rightFoot.name)
        

                
leftHand = bodypart('left hand', False, -10)

rightHand = bodypart('right hand', False, -10)

leftArm = bodypart('left arm', False, -22)

rightArm = bodypart('right arm', False, -22)

leftFoot = bodypart('left foot', False, -10)

rightFoot = bodypart('right foot', False, -10)

leftLeg = bodypart('left leg', False, -28)

rightLeg = bodypart('right leg', False, -28)

bodypartList = ['left hand', 'right hand', 'left arm', 'right arm', 'left foot', 'right foot','left leg', 'right leg']

#a variable for the first fight
extraTurn = False

#The function that determines how shia moves

def shiaMoves():
    global shiaHealth
    global playerHealth
    dec1 = random.randint(1, 100)
    dec2 = random.randint(1, 100)

    #Shia skips his turn and regenerates some health
    if dec1 < 26:
        shiaHealth += random.randint(10, 20)
        print('Shia pauses for a moment, catching his breath. \nAs you pause for a second, his injuries appear to fade slightly...')
        return

    elif dec1 > 24 and dec1 < 76:
        #Straight Right:
        if dec2 < 11:
            print('Shia squares up to you, and his right fist shoots out towards you. \nYou have a split second to make a decision: \nBlock or dodge?')
            while True:
                a = input().lower()
                if a == 'block':
                    if leftArm.dismembered:
                        print('Your bring your left arm up to defend, \nbefore realising that you no longer possess one. \nShia\'s fist crashes into you, knocking you backwards.')
                        playerHealth -= 20
                        return
                    elif leftHand.dismembered:
                        print('Your bring your left arm up to defend, \nbefore realising that your hand is missing. \nShia\'s fist crashes into your stump arm, excruciating pain follows.')
                        playerhealth -= 20
                        return
                    else:
                        #50/50
                        if random.randint(1, 120) > theOdds[0]:
                             print('You bring your arm up, knocking Shia\'s fist aside.')
                             return
                        else:
                            print('You attempt to block the punch, but Shia\'s fist slides through your guard, \nand crashes into you.')
                            playerHealth -= 10
                            return
                elif a == 'dodge':
                    #2/3 chance of failure
                    if random.randint(1, 120) < theOdds[6]:
                        print('You try to sidestep Shia\'s fist, but it slams into you nonetheless')
                        playerHealth -= 10
                        return
                    else:
                        print('You step smoothly out of the path of Shia\'s fist, leaving him stumbling.')
                        return
                else:
                    print('Please input a valid instruction (block or dodge)')
                    continue
            
        #Striaght left:
        elif dec2 < 21:
            print('Shia squares up to you, and his left fist shoots out towards you. \nYou have a split second to make a decision: \nBlock or dodge?')
            while True:
                a = input().lower()
                if a == 'block':
                    if rightArm.dismembered:
                        print('Your bring your right arm up to defend, \nbefore realising that you no longer possess one. \nShia\'s fist crashes into you, knocking you backwards.')
                        playerHealth -= 20
                        return
                    elif rightHand.dismembered:
                        print('Your bring your right arm up to defend, \nbefore realising that your hand is missing. \nShia\'s fist crashes into your stump arm, excruciating pain follows.')
                        playerhealth -= 20
                        return
                    else:
                        #50/50
                        if random.randint(1, 120) > theOdds[0]:
                             print('You bring your arm up, knocking Shia\'s fist aside.')
                             return
                        else:
                            print('You attempt to block the punch, but Shia\'s fist slides through your guard, \nand crashes into you.')
                            playerHealth -= 10
                            return
                elif a == 'dodge':
                    #2/3 chance of failure
                    if random.randint(1, 120) < theOdds[6]:
                        print('You try to sidestep Shia\'s fist, but it slams into you nonetheless')
                        playerHealth -= 10
                        return
                    else:
                        print('You step smoothly out of the path of Shia\'s fist, leaving him stumbling.')
                        return
                else:
                    print('Please input a valid instruction (block or dodge)')
                    continue
            
        #Left hook:
        elif dec2 < 31:
            print('Shia winds up for a colossal blow, his left hand whisltes through the air, \ngiving you a moment to consider your options. \nBlock or Dodge?')
            while True:
                a = input().lower()
                if a == 'block':
                    if rightArm.dismembered:
                        print('You brace your right arm for the impact of Shia\'s fist, \nbefore realising that you no longer possess one. \nShia\'s fist crashes into you, knocking you aside.')
                        playerHealth -= 25
                        return
                    elif rightHand.dismembered:
                        print('You brace your right arm for the impact of Shia\'s fist, \nbefore realising that your hand is missing. \nShia\'s fist crashes into your stump arm, excruciating pain follows.')
                        playerhealth -= 25
                        return
                    else:
                        #1/3 chance of failure
                        if random.randint(1, 120) > theOdds[6]:
                            print('You attempt to block the punch, but Shia\'s fist crashes through your guard, \nand falls into you.')
                            playerHealth -= 15
                            return
                        else:
                             print('You bring your arm up, knocking Shia\'s fist aside.')
                             return
                elif a == 'dodge':
                    #1/3 chance of failure
                    if random.randint(1, 120) > theOdds[6]:
                        print('You try to duck under Shia\'s fist, but it moves too fast, and catches you before you can escape')
                        playerHealth -= 15
                        return
                    else:
                        print('You duck smoothly under the path of Shia\'s fist, leaving him stumbling.')
                        return
                else:
                    print('Please input a valid instruction (block or dodge)')
                    continue
                
        #Right hook:
        elif dec2 < 41:
            print('Shia winds up for a colossal blow, his right hand whisltes through the air, \ngiving you a moment to consider your options. \nBlock or Dodge?')
            while True:
                a = input().lower()
                if a == 'block':
                    if leftArm.dismembered:
                        print('You brace your left arm for the impact of Shia\'s fist, \nbefore realising that you no longer possess one. \nShia\'s fist crashes into you, knocking you aside.')
                        playerHealth -= 25
                        return
                    elif leftHand.dismembered:
                        print('You brace your left arm for the impact of Shia\'s fist, \nbefore realising that your hand is missing. \nShia\'s fist crashes into your stump arm, excruciating pain follows.')
                        playerhealth -= 25
                        return
                    else:
                        #1/3 chance of failure
                        if random.randint(1, 120) > theOdds[6]:
                            print('You attempt to block the punch, but Shia\'s fist crashes through your guard, \nand falls into you.')
                            playerHealth -= 15
                            return
                        else:
                             print('You bring your arm up, knocking Shia\'s fist aside.')
                             return
                elif a == 'dodge':
                    #1/3 chance of failure
                    if random.randint(1, 120) > theOdds[6]:
                        print('You try to duck under Shia\'s fist, but it moves too fast, and catches you before you can escape')
                        playerHealth -= 15
                        return
                    else:
                        print('You duck smoothly under the path of Shia\'s fist, leaving him stumbling.')
                        return
                else:
                    print('Please input a valid instruction (block or dodge)')
                    continue
                
        #Uppercut
        elif dec1 < 51:
            print('Shia crouches, and steps forward, driving upwards with his fist. \nYou need to act. Now! \nBlock or dodge?')
            while True:
                a = input().lower()
                if a == 'block':
                    if leftArm.dismembered and rightArm.dismembered:
                        print('You lean forward, ready to stifle Shia\'s attack before it can even begin. \nBut as you move to reach down and catch Shia\'s punch, you realise you have no arms,')
                        print('\njust as Shia\'s fist catches your chin, and drives it skyward.')
                        playerHealth -= 30
                        return
                    elif (leftHand.dismembered and rightArm.dismembered) or (rightHand.dismembered and leftArm.dismembered):
                        print('You lean forward, ready to stifle Shia\'s attack before it can even begin. \nBut as you move to reach down and catch Shia\'s punch, you realise you have only one arm, and no hands.')
                        print('\njust as Shia\'s fist catches your chin, and drives it skyward.')
                        playerhealth -= 30
                        return
                    elif leftHand.dismembered and rightHand.dismembered:
                        print('You lean forward, ready to stifle Shia\'s attack before it can even begin. \nBut as you move to reach down and catch Shia\'s punch, you realise you have no hands,')
                        print('\njust as Shia\'s fist catches your chin, and drives it skyward.')
                        playerHealth -= 30
                        return
                    else:
                        #1/5 chance of failure to block
                        if random.randint(1, 120) < theOdds[3]:
                            print('You lean forward to block Shia\'s punch a moment to late, \nand his fist breezes through your defence like it doesn\'t exist, crashing into your chin.')
                            playerHealth -= 25
                            return
                        else:
                            print('You lean forward to block Shia\'s punch, stifling the blow before it gathers any power')
                            return
                            
                elif a == 'dodge':
                    #1/4 chance of failure to dodge
                    if random.randint(1, 120) < theOdds[2]:
                        print('You lean back, envisioning Shia\'s fist breezing past your face, but never touching. \nUnfortunately this is not to be, as Shia\'s fist crashes into you chin.')
                        playerHealth -= 25
                        return
                    else:
                        print('You lean back a few centimeters, and Shia\'s fist flys in front of your eyes, never touching you.')
                        return
                else:
                    print('Please input a valid instruction (block or dodge)')
                    continue

        #low kick
        elif dec1 < 61:
            print('Shia lunges forward, and drops to the ground, his leg snaking out towards you. \nYou can see the low kick coming, but what to do? \nBlock or dodge?')
            while True:
                a = input().lower()
                if a == 'block':
                    if leftLeg.dismembered and rightLeg.dismembered:
                        print('With no legs, you have no way of stopping Shia\'s low flying leg, \nand it crunches into you.')
                        playerHealth -= 25
                        return
                    elif (leftFoot.dismembered and rightLeg.dismembered) or (rightFoot.dismembered and leftLeg.dismembered):
                        print('With only one leg, and no feet, you have no way of stopping Shia\'s low flying leg, \nand it crunches into you.')
                        playerhealth -= 25
                        return
                    elif leftHand.dismembered and rightHand.dismembered:
                        print('With no feet, you have no way of stopping Shia\'s low flying leg, \nand it crunches into you.')
                        playerHealth -= 25
                        return
                    else:
                        #1/3 chance of failure to block
                        if random.randint(1, 120) < theOdds[1]:
                            print('You attempt to plant your foot over Shia\'s quickly moving leg, \nbut you mistime it slightly, and the impact shocks you like a hammer blow')
                            playerHealth -= 15
                            return
                        else:
                            print('You plant your foot over Shia\'s leg, pinning it to the ground.')
                            return
                elif a == 'dodge':
                    #2/3 chance of failure to dodge
                    if random.randint(1, 120) < theOdds[6]:
                        print('You jump, intending to clear shia\'s flying leg, but he adjusts and sweeps his leg higher, plucking you out of the air and sending you flying.')
                        playerHealth -= 15
                        return
                    else:
                        print('You jump, clearing Shia\'s leg perfectly.')
                        return
                else:
                    print('Please input a valid instruction (block or dodge)')
                    continue

        #Headbutt
        elif dec1 < 71:
            print('Shia lunges forward, and drops to the ground, his leg snaking out towards you. \nYou can see the low kick coming, but what to do? \nBlock or dodge?')
            while True:
                a = input().lower()
                if a == 'block':
                    if rightArm.dismembered and leftArm.dismembered:
                        print('You go to knock Shia\'s head aside, but realise too late that you don\'t have any arms')
                        playerHealth -= 5
                        return
                    else:
                        #1/3 chance of failure to block
                        if random.randint(1, 120) < theOdds[1]:
                            print('You sweep your elbow into the side of Shia\'s head, knocking it aside.')
                            return
                elif a == 'dodge':
                    #1/3 chance of failure to dodge
                    if random.randint(1, 120) < theOdds[1]:
                        print('You step out of Shia\'s path, but he changes direction on a dime, crashing into you.')
                        playerHealth -= 5
                        return
                    else:
                        print('You step out of Shia\'s path, and he blunders on past you.')
                        return
                else:
                    print('Please input a valid instruction (block or dodge)')
                    continue
                
        #kick to the balls
        elif dec1 < 81:
            print('Shia pivots on the ball of his foot, bringing the other one up sharply towards your groin. \nThis is dire, will you \nBlock or dodge?')
            while True:
                a = input().lower()
                if a == 'block':
                    if rightHand.dismembered or leftHand.dismembered:
                        print('You desperately bring your hands down to defend yourself, \nrealising only as Shia\'s foot crashes into your stump that one of them is missing.')
                        playerHealth -= 35
                    elif rightHand.dismembered and leftHand.dismembered:
                        print('You desperately bring your hands down to defend yourself, \nrealising only as Shia\'s foot crashes into your stump arms that you have none.')
                        playerHealth -= 35
                        return
                    else:
                        #1/3 chance of failure to block
                        if random.randint(1, 120) < theOdds[1]:
                            print('You sweep your elbow into the side of Shia\'s head, knocking it aside.')
                            return
                elif a == 'dodge':
                    #1/3 chance of failure to dodge
                    if random.randint(1, 120) < theOdds[1]:
                        print('You jerk your hands down in defence, but they provide little cushioning from Shia\'s foot.')
                        playerHealth -= 35
                        return
                    else:
                        print('You jerk your hands down in defence, and manage to fend off Shia\'s vicious foot.')
                        return
                else:
                    print('Please input a valid instruction (block or dodge)')
                    continue
        
        #Shoulder charge
        elif dec1 < 91:
            print('Shia springs forward, leaning sideways and tucking his chin down, \nhis shoulder rushes toward you with his full bodyweight behind it. \nShia is almost upon you, you need to make your move! \nBlock or dodge?')
            while True:
                a = input().lower()
                if a == 'block':
                    if rightArm.dismembered and leftArm.dismembered:
                        print('You prepare to brace against Shia\'s oncoming shoulder, but realise you don\'t have any arms')
                        playerHealth -= 20
                        return
                    else:
                        #9/10 chance of failure to block
                        if random.randint(1, 120) < theOdds[4]:
                            playerHealth -= 15
                            print('You ready yourself to absorb the force of Shia\'s charge, \nbut the impact is greater than you anticipated, and the drives through you/')
                            return
                        else:
                            print('You ready yourself to absorb the force of Shia\'s charge. \nAs he hits you, your feet slide back an inch, but you hold your ground and shove him away.')

                elif a == 'dodge':
                    #1/3 chance of failure to dodge
                    if random.randint(1, 120) < theOdds[1]:
                        print('You step out of Shia\'s path, but he changes direction on a dime, crashing into you.')
                        playerHealth -= 15
                        return
                    else:
                        print('You step out of Shia\'s path, and he blunders on past you.')
                        return
                else:
                    print('Please input a valid instruction (block or dodge)')
                    continue
        #Strangle
        else:
            print('Shia tenses on the balls of his feet for a moment, before springing forward, \nhis hands clawing for your throat.')
            while True:
                a = input().lower()
                if a == 'block':
                    if rightHand.dismembered and leftHand.dismembered:
                        print('You step inside Shia\'s flailing arms, and go to bring your hands up to his throat, \nbefore realising you have none.')
                        playerHealth -= 20
                        return
                    else:
                        #9/10 chance of failure to block
                        if random.randint(1, 120) < theOdds[4]:
                            playerHealth -= 15
                            print('You step inside Shia\'s flailing arms, and go to bring your hands up to his throat, \nsuddenly Shia\'s arms are inside yours, pushing them aside, \nand cutting of your air supply.')
                            print('After an eternity, you break free and stumble away, gasping...')
                            return
                        else:
                            print('You step inside Shia\'s flailing arms, and bring your hands up to his throat, \npushing and grasping firmly, you cut off his air supply, and send him stumbling backwards.')
                            return

                elif a == 'dodge':
                    #2/3 chance of failure to dodge
                    if random.randint(1, 120) < theOdds[6]:
                        print('You attempt to duck underneath Shia\'s arms, but he darts behind you and wraps his arms around your throat.')
                        print('After an eternity, you break free and stumble away, gasping...')
                        playerHealth -= 15
                        return
                    else:
                        print('You duck underneath Shia\'s arms, he stumbles, and rolls over your back')
                        return
                else:
                    print('Please input a valid instruction (block or dodge)')
                    continue

    #Shia attempts to eat the player
    else:
        target = random.choice(bodypartList)
        if random.randint(1, 120) > theOdds[7]:
            if target == 'left hand':
                print('Before you have time to react, Shia lunges forward, \ngrabs you by the left elbow, and sinks his teeth deep into you wrist.')
                print('Shia wrenches his head to the side, tearing your hand clean off your arm.')
                print('You stare in disbelief at what used to be your left hand, then shake your head. \nThere\'s no time for remorse if your going to get out of this alive')
                leftHand.dismember(-15)
                return
            elif target == 'right hand':
                print('Before you have time to react, Shia lunges forward, \ngrabs you by the right elbow, and sinks his teeth deep into you wrist.')
                print('Shia wrenches his head to the side, tearing your hand clean off your arm.')
                print('You stare in disbelief at what used to be your right hand, then shake your head. \nThere\'s no time for remorse if your going to get out of this alive')
                rightHand.dismember(-15)
                return
            elif target =='left arm':
                print('Faster than you can believe, Shia leaps at you, and is upon you. \nHis head flashes past the left of your head, and you feel his teeth sink into your left shoulder.')
                print('Shia\'s body tenses, and he bites hard into your shoulder. \nYou feel bone and cartilage crunch, as he tears your arms away from your body.')
                print('Shia leaps up, takes a bite from your arm and then discards it, as a dog would a bone. \nYou ready yourself for the fight to come.')
                leftArm.dismember(-30)
                return
            elif target =='right arm':
                print('Faster than you can believe, Shia leaps at you, and is upon you. \nHis head flashes past the right of your head, and you feel his teeth sink into your right shoulder.')
                print('Shia\'s body tenses, and he bites hard into your shoulder. \nYou feel bone and cartilage crunch, as he tears your arms away from your body.')
                print('Shia leaps up, takes a bite from your arm and then discards it, as a dog would a bone. \nYou ready yourself for the fight to come.')
                rightArm.dismember(-30)
                return
            elif target =='left foot':
                if rightFoot.dismember:
                    print('Shia dives down, tackling you to the ground and grabbing your left foot. \nHis teeth sink into your ankle, and you feel the bones in your shin twist against eachother.')
                    print('This pain is soon eclipsed, as Shia tears your foot from your leg, hungrily gulping down on the flesh that was once yours.')
                    print('You look up at Shia, and groan, \nknowing you must continue to fight.')
                    return
                else:
                    print('Shia dives down, tackling you to the ground and grabbing your left foot. \nHis teeth sink into your ankle, and you feel the bones in your shin twist against eachother.')
                    print('This pain is soon eclipsed, as Shia tears your foot from your leg, hungrily gulping down on the flesh that was once yours.')
                    print('You hop to your foot, and prepare to fight once again.')
                    leftFoot.dismember(-17)
                    return
            elif target =='right foot':
                if leftFoot.dismember:
                    print('Shia dives down, tackling you to the ground and grabbing your right foot. \nHis teeth sink into your ankle, and you feel the bones in your shin twist against eachother.')
                    print('This pain is soon eclipsed, as Shia tears your foot from your leg, hungrily gulping down on the flesh that was once yours.')
                    print('You look up at Shia, and groan, \nknowing you must continue to fight.')
                    return
                else:
                    print('Shia dives down, tackling you to the ground and grabbing your right foot. \nHis teeth sink into your ankle, and you feel the bones in your shin twist against eachother.')
                    print('This pain is soon eclipsed, as Shia tears your foot from your leg, hungrily gulping down on the flesh that was once yours.')
                    print('You hop to your foot, and prepare to fight once again.')
                    rightFoot.dismember(-17)
                    return
            elif target =='left leg':
                print('Shia tackels you around the waist, and before you can do anything, \nyou feel his teeth sinking into you left thigh.')
                print('Shia pushes your leg back as far as it will go, \nand gnaws hungrily at it, until the ligament snaps, and your leg goes limp.')
                print('He shifts his elbow onto your abdomen, and using the leverage gained, \nrips your leg from your torso. \nHe takes a bite, and throws your leg aside, \nready to continue the fight.')
                leftLeg.dismember(-35)
                return
            elif target =='right leg':
                print('Shia tackels you around the waist, and before you can do anything, \nyou feel his teeth sinking into you right thigh.')
                print('Shia pushes your leg back as far as it will go, \nand gnaws hungrily at it, until the ligament snaps, and your leg goes limp.')
                print('He shifts his elbow onto your abdomen, and using the leverage gained, \nrips your leg from your torso. \nHe takes a bite, and throws your leg aside, \nready to continue the fight.')
                rightLeg.dismember(-35)
                return


#Function used to determine the player's move. they can punch or kick a variety of bodyparts
#kicks to more damage but are less likely to succeed, punches do the opposite
            #Attacking bodypart should be a string, in the format of 'hand' or 'leg'

#dictionary used in the function. I'm sure there's a better way, but idk how classes work
nameToSelf = {
    'left hand' : leftHand,
    'right hand' : rightHand,
    'left arm' : leftArm,
    'right arm' : rightArm,
    'left foot' : leftFoot,
    'right foot' : rightFoot,
    'left leg' : leftLeg,
    'right leg' : rightLeg
    }



Probabilities = {
'head' : [70, 40],
'nose' : [80, 30],
'eye' : [80, 45],
'temple' : [70, 45],
'neck' : [80, 35],
'shoulder' : [100, 20], 
'sternum' : [90, 25],
'stomach' : [85, 30],
'groin' : [68, 45],
'thigh' : [100, 15],
'knee' : [90, 28],
'shin' : [100, 25],
'ankle' : [95, 22]
}
    
def playerMoves(attackingBodypart, target):
    global shiaHealh
    actualBit = ''
    Omod = 0
    Dmod = 0
    #Determining whether the right or left leg/arm is being used, and if the player has neither, ending the function.
    if nameToSelf['right ' + attackingBodypart].dismembered and nameToSelf['left ' + attackingBodypart].dismembered:
        if attackingBodypart == 'foot':
            print('You ready yourself to attack, and then catch yourself... \nYou don\'t have any feet, and you\'ve wasted this opportunity.')
        else:
            print('You ready yourself to attack, and then catch yourself... \nYou don\'t have any ' + attackingBodypart + 's and you\'ve wasted this opportunity.')
        return None
    elif nameToSelf['right ' + attackingBodypart].dismembered:
        actualBit = nameToSelf['left ' + attackingBodypart]
    else:
        actualBit = nameToSelf['right ' + attackingBodypart]

    if 'hand' or 'arm' in attackingBodypart:
        Omod += 10
        Dmod += 10
    else:
        Omod -= 10
        Dmod += 10

    if random.randint(1, 120) < (Probabilities[target][0] + Omod):
        global shiaHealth
        shiaHealth -= (Probabilities[target][1] + Dmod)
        return True
    else:
        return False
            

 

        

a = input().lower()
while a != '!skip':
    if 'help' in a:
        help_()
        a = input()
    elif 'go' in a:
        print('------')
        print('You\'re walking in the woods,\nthere\'s no one around and your phone is dead. \nout of the corner of your eye you spot him\n... \n... \nShia Labeouf.')
        break
    else:
        print('type something else bub')



#----------------------------------------------------
#WOODS1

#place variable stores where the player is
place = 'woods1'
a = ''
print('He\'s following you, \'bout thirty feet back, \nHe gets down on all fours and breaks into a sprint. \nHe\'s gaining on you!')
a = input().lower()
#looked variable... To see if the player has looked.
looked = False
while a != '!skip':
    #look and see shia
    if 'look' in a and looked == False:
        print('You\'re looking for your car, but you\'re all turned around \nHe\'s almost upon you now and you can see there\'s blood on his face \nBy God there\'s blood everywhere!')
        looked = True
        a = input().lower()
    #look again and die
    elif 'look' in a and looked == True:
        print('You turn to look once again, and before you know it he is upon you! \nYou feel his teeth sink into your neck, and a sharp pain in your kidneys.')
        death()
    #run toward shia and die
    elif ('run' or 'walk' or 'sneak' in a) and check_direction(to_list, a) and check_direction(at_shia, a):
        print('As you approach Shia, he opens his arms and embraces you. \nYou feel safe for a second, until you feel a knife sliding through your ribs, \nand his teeth sink into your neck.')
        death()
    #walk away from shia, die
    elif 'walk' in a:
        print('You turn and walk hurridly away from Shia, Struggling to keep up the pretence of calm.')
        print('You can hear his footsteps growing louder behind you, \nIn your haste you trip on a fallen brach, falling at Shia\'s feet.')
        print('His knee falls heavily into the small of your back, jarring your spine. \nYou feel his teeth on the back of your neck, \nThen lose conciousness as your spinal cord is ripped from beneath your skin.')
        death()
    #sneak for some reason, die
    elif 'sneak' in a:
        print('He has already seen you. \nYour hesitation is your demise, as he pounces on you \nRipping your oesophagus clean out of your neck.')
        death()
    #run away from shia
    elif ('run' in a) and check_direction(away_list, a):
        running_for_your_life()
        break
    #If they just type 'run'
    elif a == 'run':
        print('Run where?')
        a = input()
        if check_direction(away_list, a) or (check_direction(away_list, a) and check_direction(at_shia, a)):
            running_for_your_life()
            break
        elif check_direction(to_list, a) and check_direction(at_shia, a):
            print('As you approach Shia, he opens his arms and embraces you. \nYou feel safe for a second, until you feel a knife sliding through your ribs, \nand his teeth sink into your neck.')
            death()
        else:
            print('I don\'t understand where you want to run, \nwhat did you want to do?')
    #if they try and attack
    elif check_direction(fight_list, a):
        print('UNFINISHED (you try to fight shia and die)')
    #if they want help
    elif a == 'help':
        help()
        a = input().lower()
    elif a == 'walk' or a == 'run' or a == 'sneak':
        print('Please use the input format: <walk/sneak/run> <destination>')
        a = input().lower()
    else:
        print('Sorry, what? (I don\'t understand)')
        a = input().lower()

#----------------------------------------------------
#DARK WOODS

#this bit should only be reached if the player has escaped woods1
print('What to do now...')
place = 'dark woods'
looked = False

#A variable to be set to true when the player has exited the forest in such a way that they are about to fall on a bear trap
bear_ready = False
#If the player ran toward the light
ran = False

a = input().lower()
while a != '!skip':
    #first look
    if 'look' in a and looked == False:
        print('You scan your surroundings... \nThe woods around you feel dark and forboding \nTo the west you can barely spot the last rays of the sun, \nas it slips beneath the horizon, \nBut to the South! A faint light shines.')
        looked = True
        a = input().lower()
    #second look
    elif 'look' in a and looked == True:
        print('The definition of insanity is doing the same thing over and over again, but expecting different results')
        a = input().lower()
    #walking towards the light, or south
    elif (('walk' in a) and check_direction(to_list, a) and ('light' or 'south' in a)) or (a == 'walk south'):
        print('you walk towards the light... \nIt gradually grows brighter, \nand you can begin to make out the shape of a cottage \nYou move stealthily toward it...')
        bear_ready = True
        break
    #moving away from the light, or in any direction other than south (UNFINISHED!!!)
    elif ((('walk' or 'sneak' or 'run') in a) and check_direction(away_list, a) and ('light' or 'south' in a)):
        print('UNFINISHED idk whether you just get lost or what but for now just have another go')
        a = input().lower()
    #running towards the light, or south
    elif (('run' in a) and check_direction(to_list, a) and ('light' or 'south' in a)) or (a == 'run south'):
        print('You run desperately towards the light, \nIt gradually grows brighter \nand you can begin to make out the shape of a cottage')
        bear_ready = True
        ran = True
        break
    #sneaking towards the light, or south
    elif ('sneak' in a) and check_direction(to_list, a) and ('light' or 'south' in a) or a == 'sneak south':
        print('You creep silently through the underbrush \nA-ha! In the distance \nA small cottage with a light on. Hope! \nYou move stealthily toward it...')
        bear_ready = True
        break
    elif a == 'help':
        help_()
        a = input().lower()
    elif a == 'walk' or a == 'run' or a == 'sneak':
        print('Please use the input format: <walk/sneak/run> <destination>')
        a = input().lower()
    else:
        print('input not understood')
        a = input().lower()

if bear_ready and ran:
    print('You run desperately to the cottage, \nbut just as you begin to make out the shape of someone sitting inside, \nyour foot catches on a fallen branch.')
    print('As you fall, you catch a glimpse of something glinting on the ground, \nA breif moment of confusion is your last memory, \nas your head crashes down on the plate of a bear trap.')
    death()
elif bear_ready:
    print('But your leg! AH! It\'s caught in a bear trap!')


#----------------------------------------------------
#BEAR WOODS
    
bear_survived = False

#TE is turns elapsed. When it reaches 5, the player dies of blood loss. If the player escapes the bear trap, then bear_survived is set to true.
TE = -1

te = ['Your glance at your left leg, and quickly avert your eyes, \nfighting the urge to throw up.',
      'You watch, mesmerised for a moment, \nas the blood continues to pump from your leg.',
      'The ground around you is stained red, \nthe same colour as the horizon, stained by the dying sun.',
      'You notice that the blood flowing from your leg seems to have slowed, \nyou stare into the gory mouth of the bear trap and doze off for a minute, \nwaking with a start.',
      'Your body is growing number by the minute. \nYou know that if you do not escape the trap soon, you will perish.',
      'You attempt to move, but your head spins and you fall back, nauseated. \nYou can feel your strength slipping away, as the world slowly fades into black around you.']
      



a = input().lower()
while a != '!skip':
    #the death condition
    if TE > 3:
        print('You attempt to move, but your head spins and you fall back, nauseated. \nYou can feel your strength slipping away, as the world slowly fades into black around you.')
        death()
    #The player decides to gnaw/eat their leg off, this is the 'correct' path
    elif ('leg' in a) and check_direction(eat_list, a):
        print('Gnawing off your leg \n(Quiet, quiet)')
        print('Limping toward the cottage, \n(Quiet, quiet) \nNow you\'re on the doorstep, \nSitting inside, Shia LaBeouf. \nSharpening an axe, \n(Shia LaBeouf)')
        leftLeg.dismember(0)
        break
    #player tries to stand up
    elif a in up_list:
        print('You attempt to stand, but your bad leg buckles, \nand the weight of the bear trap pulls you down to earth')
        TE += 1
        print(te[TE])
        a = input().lower()
    #player tries to open or tear off the trap
    elif check_direction(off_trap_list, a):
        print('You try to pry open the trap, but you can\'t get any purchase on the bloodied metal.')
        TE += 1
        print(te[TE])
        a = input().lower()
    #player looks around
    elif 'look' in a:
        print('To the south, you can make out a cottage, its lights glowing invitingly, \nbut the woods around you are dark and menacing.')
        TE += 1
        print(te[TE])
        a = input().lower()
    #The player tries to crawl somewhere (this has a bleed penalty of 2)
    elif 'crawl' in a.split(' '):
        print('You begin to drag yourself along the rough forest floor, \nThe heavy bear trap catches on a root, \nand the trap bites into your leg anew, \nas even more blood gushes out.')
        TE += 2
        print(te[TE])
        a = input().lower()
    #Trying to go somewhere
    elif 'walk' in a or 'run' in a or 'sneak' in a:
        print('You try to pull yourself upright, \nbut you damaged left leg collapses beneath you.')
        TE += 1
        print(te[TE])
        a = input().lower()
    #help
    elif a == 'help':
        help_()
        a = input().lower()
    else:
        print('you wut mate (i dont understand)')
        a = input().lower()
    
#----------------------------------------------------
#COTTAGE

#This bit should only be reached after a survivable encounter with the bear trap

print('What will you do now?')
#While the player hasn't yet started the fight
extraTurn = False
turn = 0
kill = False
a = input().lower()
while a != '!skip':
    if turn > 3:
        print('Shia gives his axe one last scrape of the whetstone, \nthen stiffens, sensing something is worng. \nYou freeze, and quicker than you can believe, \nShia hefts his axe at your head. \nHe does not miss.')
        death()

    if kill == True:
        break
    
    if a == 'look':
        print('You can see Shia inside, completely focused on his axe. \nHis back is to you, if you snuck in now... \nHe wouldn\'t see you.')
        turn += 1
        a = input().lower()
    #If they try to do something from the doorway
    elif check_direction(fight_list, a) and check_direction(at_shia, a):
        print('You won\'t be able to do that from the doorway will you?')
        a = input().lower()
    #Running at shia
    elif 'run' in a and (check_direction(cottage_list, a) or (check_direction(at_shia, a))):
        print('Throwing stealth to the wind, \you charge at Shia. \nHe turns, and his eyes widen as he discerns your intention. \nYou collide, and are both sent sprawling, \nhis axe flies out the window, forgotten.')
        print('Time to fight!')
        theOdds = ranIn
        break
    elif 'walk' in a and (check_direction(cottage_list, a) or ('behind shia' or 'to shia' in a)):
        print('You walk calmly into the cottage, footsteps echoing on the hardwood floor. \nShia stands, and smiles, throwing his axe aside. \nIt\'s time to fight, and you no longer have the element of suprise.')
        theOdds = walkedIn
        break
    elif  a == 'sneak inside' or ('sneak' in a and (check_direction(cottage_list, a) or ('behind shia' or 'to shia' in a))):
        theOdds = snuckIn
        print('You creep silently into the cottage, crouching behind Shia\'s chair.')
        turn += 1
        a = input().lower()
        #while the player is undetected/the fight has not started
        while a != '!skip':
            if turn > 3:
                print('Shia gives his axe one last scrape of the whetstone, \nthen stiffens, sensing something is worng. \nYou freeze, and quicker than you can believe, \nShia hefts his axe at your head. \nHe does not miss.')
                death()

            if kill == True:
                break

            if a == 'look':
                print('Now inside the cottage, you look around, finding it confusingly barren. \nIt contains little more than Shia and his axe.')
                turn += 1
                a = input().lower()
            elif ('strangle' in a or 'choke' in a) and check_direction(at_shia, a):
                shiaHealth -= 60
                print('You wrap your arms around Shia\'s neck, and squeeze with all you might. \nHe struggles, and eventually shakes you off, massaging his neck.')
                print('Time to fight!')
                kill = True
                break
            #If they try to leave the cottage
            elif check_direction(away_list, a):
                print('You turn, suddenly overcome by panic you sprint, crashng through the underbrush, \nJust as Shia\'s axe crashes into you head.')
                death()
            elif ('tip' and 'chair') in a:
                 print('You give Shia\'s chair a mighty heave, sending him sprawling onto the floor. \nNow is your chance to strike!')
                 extraTurn = True
                 break
            elif 'hit' in a:
                #making querying where the player wants to hit Shia easier
                while a != '!skip':
                    if 'head' in a:
                        print('You lash out against Shia\'s head with your fist. \nHis axe clatters to the ground, and he turns on you, \nready to fight.')
                        shiaHealth -= 45
                        kill = True
                        break
                    elif 'temple' in a:
                        print('Your fist arcs viciously into the side of Shia\'s head. \nHis axe clatters to the ground, and he turns on you, \nready to fight.')
                        shiaHealth -= 50
                        kill = True
                        break
                    elif 'neck' in a:
                        print('You lash out with all you might against the back of Shia\'s neck. \nHe drops his axe and advances on you, more angry than injured.')
                        shiaHealth -= 35
                        kill = True
                        break
                    elif ('torso' or 'leg' or 'arm' or 'foot' or 'shoulder' or 'rib') in a:
                        print('There is a chair in the way, pick another bodypart to attack.')
                        a = input().lower()
                    else:
                        print('You can\'t hit that.')
                        a = input().lower()
    else:
        print('Please input a valid instruction')
        a = input().lower()


#while the fight is ongoing
a = ''
while a != '!skip':
    if playerHealth == 0:
        print('This, as it turns out, is your deathblow. Better luck next time.')
        death()
    elif shiaHealth == 0:
        print('------ \n------ \nFighting for your life with Shia Labeouf, \nWrestling a knife from Shia Labeouf, \nStab it in his kidney. \nSafe at last from Shia Labeouf.')
        print('You limp into the dark woods, \nBlood oozing from your stump leg. \nYou\'ve won. You have beaten Shia Labeouf.')
        break

    #Wow, boolean is not a boolean value. How strange...
    boolean = None

    if extraTurn == False:
        shiaMoves()
    elif extraTurn == True:
        extraTurn = False
    

    a = input().lower()

    if 'punch' in a and 'nose' in a:
        boolean = playerMoves('hand', 'nose')
        if boolean:
            print('Your fist shoots out towards Shia\'s nose, \nsnapping his head backwards.')
            continue
        elif not boolean:
            print('Your fist shoots out towards Shia\'s nose, \nbut he knocks you fist aside.')
            continue
        else:
            print('You make ready to strike Shia with your fists, \nBut catch yourself before attacking, realising that you don\'t have any hands. \nYou\'ve wasted this opportunity.')
            continue

    elif 'kick' in a and 'nose' in a:
        boolean = playerMoves('foot', 'nose')
        if boolean:
            print('In one smooth motion, you raise your foot and launch it at Shia\'s nose, \nsnapping his head backwards.')
            continue
        elif not boolean:
            print('YIn one smooth motion, you raise your foot and launch it at Shia\'s nose Shia\'s nose, \nunfortunately, he sidesteps you blow with ease.')
            continue
        else:
            print('You make ready to strike Shia with your foot, \nBut catch yourself before attacking, realising that you don\'t have any feet. \nYou\'ve wasted this opportunity.')
            continue

    elif 'punch' in a and 'eye' in a:
        boolean = playerMoves('hand', 'eye')
        if boolean:
            print('Your hand shoots out towards Shia\'s eye, \nyou jab two fingers into each of Shia\'s eyes, and he doubles over in pain.')
            continue
        elif not boolean:
            print('Your fist shoots out at Shia\'s face, \nbut he knocks you fist aside.')
            continue
        else:
            print('You make ready to jab Shia in the eyes, \nBut catch yourself before attacking, realising that you don\'t have any hands. \nYou\'ve wasted this opportunity.')
            continue

    elif 'kick' in a and 'eye' in a:
        boolean = playerMoves('foot', 'eye')
        if boolean:
            print('In one smooth motion, you raise your foot and launch it at Shia\'s face, \nblackening his eye.')
            continue
        elif not boolean:
            print('In one smooth motion, you raise your foot and launch it at Shia\'s nose Shia\'s nose, \nunfortunately, he sidesteps you blow with ease.')
            continue
        else:
            print('You make ready to strike Shia with your foot, \nBut catch yourself before attacking, realising that you don\'t have any feet. \nYou\'ve wasted this opportunity.')
            continue

    elif 'punch' in a and 'temple' in a:
        boolean = playerMoves('hand', 'temple')
        if boolean:
            print('You wind up, and launch your fist at Shia\'s head. \nStriking him square on the temple, and sending him stumbling.')
            continue
        elif not boolean:
            print('Your fist shoots out at Shia\'s face, \nbut he ducks under it.')
            continue
        else:
            print('You wind up to launch your fist at Shia, \nbefore realising that you don\'t have any hands. You\ve wasted this opportunity.')
            continue

    elif 'kick' in a and 'temple' in a:
        boolean = playerMoves('foot', 'temple')
        if boolean:
            print('You launch your foot at the side of Shia\'s head, \nknocking him to the ground.')
            continue
        elif not boolean:
            print('You launch your foot at the side of Shia\'s head, \nbut he ducks under your blow.')
            continue
        else:
            print('You make ready to strike Shia with your foot, \nBut catch yourself before attacking, realising that you don\'t have any feet. \nYou\'ve wasted this opportunity.')
            continue

    elif 'punch' in a and 'neck' in a:
        boolean = playerMoves('hand', 'neck')
        if boolean:
            print('You lash your fist into Shia\'s neck, \nhe coughs, suprised.')
            continue
        elif not boolean:
            print('You lash your fist at Shia\'s neck, \nBut he intercepts your blow with ease.')
            continue
        else:
            print('You wind up to launch your fist at Shia, \nbefore realising that you don\'t have any hands. You\ve wasted this opportunity.')
            continue

    elif 'kick' in a and 'neck' in a:
        boolean = playerMoves('foot', 'neck')
        if boolean:
            print('You snap your foot into Shia\'s neck, \nhe splutters, and staggers backwards.')
            continue
        elif not boolean:
            print('You snap your foot at Shia\'s neck, \nBut he intercepts your blow with ease.')
            continue
        else:
            print('You make ready to strike Shia with your foot, \nBut catch yourself before attacking, realising that you don\'t have any feet. \nYou\'ve wasted this opportunity.')
            continue
        
    elif 'punch' in a and 'shoulder' in a:
        boolean = playerMoves('hand', 'shoulder')
        if boolean:
            print('You fire your fist into Shia\'s shoulder, \nknocking him side on.')
            continue
        elif not boolean:
            print('You fire your fist at Shia\'s shoulder, \nBut he intercepts your blow with ease.')
            continue
        else:
            print('You prepare to shoot your fist into Shia, \nbut realise that you have no hands. \nYou\'ve wasted this opportunity.')
            continue
        
    elif 'kick' in a and 'shoulder' in a:
        boolean = playerMoves('foot', 'shoulder')
        if boolean:
            print('You snap your foot into Shia\'s shoulder, \nthe blow spinning him around like a top.')
            continue
        elif not boolean:
            print('You snap your foot at Shia\'s shoulder, \nBut he intercepts your blow with ease.')
            continue
        else:
            print('You make ready to strike Shia with your foot, \nBut catch yourself before attacking, realising that you don\'t have any feet. \nYou\'ve wasted this opportunity.')
            continue
        
    elif 'punch' in a and 'sternum' in a:
        boolean = playerMoves('hand', 'shoulder')
        if boolean:
            print('You step forward, sinking your fist into the space just below Shia\'s ribs. \nShia coughs, momentarily winded.')
            continue
        elif not boolean:
            print('You step forward, looking to sink your fist into Shia\'s sternum, \nbut he cuts your strike off at the elbow.')
            continue
        else:
            print('You prepare to sink your fist into Shia, \nbut realise that you have no hands. \nYou\'ve wasted this opportunity.')
            continue
        
    elif 'kick' in a and 'sternum' in a:
        boolean = playerMoves('foot', 'sternum')
        if boolean:
            print('You slam your heel into Shia\'s sternum, \nsending him stumbling backwards.')
            continue
        elif not boolean:
            print('You slam your heel at Shia\'s midriff, \nbut he uses his arm to deflect your blow.')
            continue
        else:
            print('You make ready to strike Shia with your foot, \nBut catch yourself before attacking, realising that you don\'t have any feet. \nYou\'ve wasted this opportunity.')
            continue
        
    elif 'punch' in a and 'stomach' in a:
        boolean = playerMoves('hand', 'shoulder')
        if boolean:
            print('You step forward, sinking your fist into Shia\'s stomach. \nShia double over, momentarily winded.')
            continue
        elif not boolean:
            print('You step forward, looking to sink your fist into Shia\'s stomach, \nbut he cuts your strike off at the elbow.')
            continue
        else:
            print('You prepare to sink your fist into Shia, \nbut realise that you have no hands. \nYou\'ve wasted this opportunity.')
            continue
        
    elif 'kick' in a and 'stomach' in a:
        boolean = playerMoves('foot', 'stomach')
        if boolean:
            print('You slam your heel into Shia\'s stomach, \nsending him stumbling backwards.')
            continue
        elif not boolean:
            print('You slam your heel at Shia\'s midriff, \nbut he uses his arm to deflect your blow.')
            continue
        else:
            print('You make ready to strike Shia with your foot, \nBut catch yourself before attacking, realising that you don\'t have any feet. \nYou\'ve wasted this opportunity.')
            continue
        
    elif 'punch' in a and ('groin' in a or 'balls' in a):
        boolean = playerMoves('hand', 'groin')
        if boolean:
            print('You step forward, sinking your fist into Shia\'s groin. \nShia double over, stunned.')
            continue
        elif not boolean:
            print('You step forward, looking to sink your fist into Shia\'s groin, \nbut he cuts your strike off at the elbow.')
            continue
        else:
            print('You prepare to sink your fist into Shia, \nbut realise that you have no hands. \nYou\'ve wasted this opportunity.')
            continue
        
    elif 'kick' in a and ('groin' or 'balls') in a:
        boolean = playerMoves('foot', 'groin')
        if boolean:
            print('You sink your foot up into Shia\'s groin, \nhe almost collapses, barely managing to remain upright.')
            continue
        elif not boolean:
            print('You attempt to sink your foot up into Shia\'s groin, \nbut he scampers desperately out of the way.')
            continue
        else:
            print('You make ready to strike Shia with your foot, \nBut catch yourself before attacking, realising that you don\'t have any feet. \nYou\'ve wasted this opportunity.')
            continue
        
    elif 'punch' in a and 'thigh' in a:
        boolean = playerMoves('hand', 'thigh')
        if boolean:
            print('You step sharply downards, cutting into Shia\'s thigh with your fist.')
            continue
        elif not boolean:
            print('You step sharply downwards, attempting to strike at Shia\'s thigh, \nonly to have your punch cut off at the wrist.')
            continue
        else:
            print('You prepare to slam your fist into Shia, \nonly to realise that you have no hands. \nYou\'ve wasted this opportunity.')
            continue
        
    elif 'kick' in a and 'thigh' in a:
        boolean = playerMoves('foot', 'thigh')
        if boolean:
            print('You raise you leg, and stamp down on Shia\'s thigh, pushing him down to one knee.')
            continue
        elif not boolean:
            print('You raise you leg, and stamp down towards Shia\'s thigh, \nbut Shia moves, and your foot comes down on air.')
            continue
        else:
            print('You make ready to strike Shia with your foot, \nBut catch yourself before attacking, realising that you don\'t have any feet. \nYou\'ve wasted this opportunity.')
            continue
        
    elif 'punch' in a and 'knee' in a:
        boolean = playerMoves('arm', 'knee')
        if boolean:
            print('You plant your elbow into the side of Shia\'s knee, sending him stumbling.')
            continue
        elif not boolean:
            print('You step sharply downwards, attempting to strike at Shia\'s thigh, \nonly to have your punch cut off at the wrist.')
            continue
        else:
            print('You prepare to slam your fist into Shia, \nonly to realise that you have no hands. \nYou\'ve wasted this opportunity.')
            continue
        
    elif 'kick' in a and 'knee' in a:
        boolean = playerMoves('foot', 'knee')
        if boolean:
            print('You whip your foot around into the side of Shia\'s knee, \nand are rewarded by a shriek of pain.')
            continue
        elif not boolean:
            print('You whip your foot around at the side of Shia\'s knee, but he jumps, clearing your leg.')
            continue
        else:
            print('You make ready to strike Shia with your foot, \nBut catch yourself before attacking, realising that you don\'t have any feet. \nYou\'ve wasted this opportunity.')
            continue

    elif 'punch' in a and 'shin' in a:
        boolean = playerMoves('hand', 'shin')
        if boolean:
            print('You plant your elbow into the side of Shia\'s knee, sending him stumbling.')
            continue
        elif not boolean:
            print('You step sharply downwards, attempting to strike at Shia\'s thigh, \nonly to have your punch cut off at the wrist.')
            continue
        else:
            print('You prepare to slam your fist into Shia, \nonly to realise that you have no hands. \nYou\'ve wasted this opportunity.')
            continue
        
    elif 'kick' in a and 'shin' in a:
        boolean = playerMoves('foot', 'shin')
        if boolean:
            print('You drive your foot into Shia\'s shin, \nleaving him favouring his other leg..')
            continue
        elif not boolean:
            print('You drive your foot towards Shia\'s shin, \nbut he knocks the blow aside.')
            continue
        else:
            print('You make ready to strike Shia with your foot, \nBut catch yourself before attacking, realising that you don\'t have any feet. \nYou\'ve wasted this opportunity.')
            continue
        
    elif 'punch' in a and 'ankle' in a:
        boolean = playerMoves('hand', 'ankle')
        if boolean:
            print('You grab Shia\'s anke, flipping him onto his head.')
            continue
        elif not boolean:
            print('You go to grab Shia\'s ankle, and are rewarded with a sharp stamp on the wrist.')
            continue
        else:
            print('You prepare to slam your fist into Shia, \nonly to realise that you have no hands. \nYou\'ve wasted this opportunity.')
            continue
        
    elif 'kick' in a and 'ankle' in a:
        boolean = playerMoves('foot', 'thigh')
        if boolean:
            print('You raise you leg, and stamp down on Shia\'s ankle, \nsending him hopping away.')
            continue
        elif not boolean:
            print('You raise you leg, and stamp down towards Shia\'s ankle, \nbut only make contact with the floor.')
            continue
        else:
            print('You make ready to strike Shia with your foot, \nBut catch yourself before attacking, realising that you don\'t have any feet. \nYou\'ve wasted this opportunity.')
            continue
    elif a == 'help':
        #just reusing the variable
        help_()
        extraTurn = True
        a = input().lower()
    else:        
        print('Please enter a valid input (punch or kick [a bodypart])')
        extraTurn = True








