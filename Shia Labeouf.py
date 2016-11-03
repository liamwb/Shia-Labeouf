import sys

print('Welcome to the Shia Lebeouf experience. \nFor help type \'help\', or to begin type \'go!\'')

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
at_shia = ['him', 'shia', 'shia lebeouf']
#a list of things people might use to go *to* something
to_list = ['to', 'towards', 'toward', 'at',]
#a list of things people might use to move *away* from something
away_list = ['away', 'from', 'back']
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


#organised as location : [ways you can go from there]
areas = {'woods1' : ['east'], 'dark woods' : ['west', 'south'], 'bear woods' : ['north', 'south'], 'cottage' : ['north', 'east'], 'winning woods':''}

def help_():
    print('Type \'look\' to look around at your surroundings.')
    print('Type \'walk to [a place]\' to walk there, or \'run\' to run there')
    print('Typing \'sneak to [a place]\' will have you slowly move there, without alerting enemies.')
    print('Typing \'go\' will begin your adventure!')

#a function that checks if the player is walking in a given direction (eg. to something)
#well actually it just checks all the words in a string to see if there is a matching word in a list
    #so i don't know why i called it check_direction, it should really have been check_match or something
def check_direction(list, string):
               yep = False
               string = string.split(' ')
               for item in string:
                   for i in list:
                       if item == i:
                           return True
               return False


a = input().lower()
while a != '!skip':
    if 'help' in a:
        help_()
        a = input()
    elif 'go' in a:
        print('------')
        print('You\'re walking in the woods,\nthere\'s no one around and your phone is dead. \nout of the corner of your eye you spot him\n... \n... \nShia Lebeouf.')
        break

#----------------------------------------------------
#WOODS1

#place variable stores where the player is
place = 'woods1'
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
    #if they try and attack
    elif check_direction(fight_list, a):
        print('UNFINISHED (you try to fight shia and die)')
    #if they want help
    elif a == 'help':
        help()
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
        print('You scan your surroundings... \nThe woods around you feel dark and forboding \nTo the west you can barely spot the last rays of the sun, \nas it slips beneath the horizon, \nBut to the South! A faint light shines')
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
    else:
        print('input not understood')
        a = input().lower()

if bear_ready and ran:
    print('You run desperately to the cottage, \nbut just as you begin to make out the shape of someone sitting inside, \nyour foot catches on a fallen branch.')
    print('As you fall, you catch a glimpse of something glinting on the ground, \nA breif moment of confusion is your last memory, \nbefore your head crashes down on the plate of a bear trap.')
    death()
elif bear_ready:
    print('But your leg! AH! It\'s caught in a bear trap!')
else:
    print('liam u done fuqed up')
    a = input().lower()

#----------------------------------------------------
#BEAR WOODS
    
bear_survived = False

#TE is turns elapsed. When it reaches 6, the player dies of blood loss. If the player escapes the bear trap, then bear_survived is set to true.
TE = -1

te = ['Your glance at your leg, and quickly avert your eyes, \nfighting the urge to throw up.',
      'You watch, mesmerised for a moment, \nas the blood continues to pump from your leg.',
      'Your leg continues to bleed, \nyour hands feel numb, but at least the pain is beginning to receed.',
      'The ground around you is stained red, \nthe same colour as the horizon, stained by the dying sun.',
      'You notice that the blood flowing from your leg seems to have slowed, \nyou stare into the gory mouth of the bear trap and doze off for a minute, \nwaking with a start.',
      'Your body is growing number by the minute. \nYou know that if you do not escape the trap soon, you will perish.']
      



a = input().lower()
while a != '!skip':
    #the death condition
    if TE > 5:
        print('You attempt to move, but your head spins and you fall back, nauseated. \nYou can feel your strength slipping away, as the world slowly fades into black around you.')
        death()
    #The player decides to gnaw/eat their leg off, this is the 'correct' path
    elif ('leg' in a) and check_direction(eat_list, a):
        print('UNFINISHED TEXT (you dun gud)')
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
    else:
        print('you wut mate (i dont understand)')
        a = input().lower()
    
#----------------------------------------------------
#COTTAGE

#This bit should only be reached after a survivable encounter with the bear trap
print('Gnawing off your leg \n(Quiet, quiet.)')
print('Limping toward the cottage \n(Quiet, quiet.)')
print('Sitting inside, Shia Labeouf.')

print('Now there is a fight scene that is not yet implemented \nWould you like to (w)in the fight or (d)ie?')
a = input().lower()
if a == 'd':
    death()
elif a == 'w':
    None
else:
    print('invalid input')
    a = input().lower()

#----------------------------------------------------
#WINNING WOODS

#This bit should only be reached after beating shia up
print('second fight scene,  also not implemented yet \nWould you like to (w)in the fight or (d)ie?')
a = input().lower()
if a == 'd':
    death()
elif a == 'w':
    None
else:
    print('invalid input')
    a = input().lower()






