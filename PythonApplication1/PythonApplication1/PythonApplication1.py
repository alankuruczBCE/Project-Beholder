﻿#-----------------------------------IMPORTS----------------------------------¦
import time, windowFunction, random

#-----------------------------------VARIABLES--------------------------------¦
health = 50
level = 1.0
xp = 0
power = 9999
location = 0
section = 1
location = 1
locationName = "Test"
selection = 0
randomEnemy = 0
enemyHealth = 100
enemyPower = 10
enemyState = "def" #USE RANDOM TO CHANGE IN BATTLE
sectionReal = 0
listHistory = []
xpNeeded = 75
inventory = [["Apple", 5],["Apple", 5]]
apple = ["Apple", 5]
HeartyStew = ["Mysterious Stew", -99999]
slopList = ["john pork", "skibidi", "toilet", "soy", "wojak", "baby gronk"
            , "friend", "kris", "senan", "roblox", "homestuck", "speed", 
            "fanum", "brainrot", "camera", "mario", "chud", "chad", 
            "costco", "among us", "sus", "mewing", "sigma", "hawk", 
            "tuah", "haircut"]#LIST TO STOP ENTRY OF BRAINROT NAMES
codeList = ["LEVELOFF", "NOGAME", "FASTSPEED"]
slopFree = 0
sectionPause = 0
tick = 0
levelLock = 0
amountFights = 0
selfPower = 5
healthInitial = 50
#-------------------------------PARAMETERS-----------------------------------¦
level_requirement = 1
area_enabled = 1
slopFree = 0


# FUNCTION DECLARATIONS
def respond_(responseWords = "test", responseText = "What do you respond " 
             "with?    "):
    global tick
    print()
    print()
    response = input(responseText)
    tick = 0
    print()
    print()
    responseLength = len(responseWords)
    for i in range(responseLength):
        if responseWords[i] in response.lower():
            tick = 1
    return response


class Weapon:
    def __init__(self, index, name, damage, description, active):
        self.index = index
        self.name = name
        self.damage = damage
        self.description = description
        self.active = active

    def summary(self):
        print(self.index, ":", self.name, "  Damage: ", str(self.damage), 
              "\nDescription:  ", self.description)

RustyBlade = Weapon(1,"Rusty Training Blade", 20, 
"It may or may not do the job. "
"I don't think it will but it's up to you.", True)
CrazyBlade = Weapon(2,"Basic Basher", 40, "A basic sword. "
                    "It works somewhat well", False)
equipped = RustyBlade
power = equipped.damage
class Enemy:
    def __init__(self):
        self.health = 100
        self.power = 20
        self.state = "Defend"
        self.lockbuffer = 0


    def enemyStateChoose_(self):
        enemyStates = ("Attack", "Defend")
        self.state = random.choice(enemyStates)

def areaLevel_(): #MAIN GAMEPLAY FUNC
    global section
    global location
    global locationName
    global selection #MAKE VARIABLES GLOBAL
    global sectionReal
    global sectionPause
    global area_enabled
    global amountFights
    if area_enabled == 1:
        xpNeeded = ((50**(1 + (level * 0.05))))

        windowFunction.ClearFrame_()
        print("Level: " + str(level) + "            " + "XP - " + str(xp) + 
              "             " + "XP until level", str(int(level) + 1)
             + " -", str(round(xpNeeded) - xp)) #PRINT STATS
        

        if section in range(0,6): #CALCULATE SECTION
            location = 1
        elif section in range(6, 11):
            location = 2

        if location == 1: #FIND LOCATION NAME, SELECT INDEX FOR PRINTING
            locationName = "Granfield"
            index = 0
        elif location == 2:
            locationName = "Granfield - Hills"
            index = 1
        elif location == 3:
            locationNmae = "Vesenid"
            index = 2

        sectionReal = section - ((location-1) * 5) #CALCULATE DISPLAY SECTION
        print(locationName, "-", str(sectionReal)) #PRINT DISPLAY SECTION

        windowFunction.locationArt(index) #PRINT LOCATION ART

    
        if level - 1 >= section or level_requirement == 0:
            print("1 - Fight \n2 - View Inventory \n3 - Progress \n"
                  "4- Add an Apple")#PRINT OPTIONS
        else:
            print("1 - Fight \n2 - View Inventory \n3 - "
                  "(NEED TO LEVEL UP TO PROGRESS) \n4- Add an Apple")
                    #PRINT OPTIONS

        selection = input("") #SELECTION DETECTION CODE
        if selection == "1":
            searchArea_()
        elif selection == "2":
            inventory_()
        elif selection == "3":
            amountFights = 0
            levelLock = 0
            if section == 5 or section == 10 or section == 15\
                or section == 20 or section == 25:
                section = section + 1
                return
            if level - 1 >= section:
                section = section + 1
            areaLevel_()
        elif selection == "4":
            addItem_(inventory, apple)
            areaLevel_()
        else:
            areaLevel_()
    else:
        pass

def addItem_(listicle,element):
    listicle.append(element)
    return 1


def searchArea_():
    global levelLock
    global amountFights
    if amountFights > 9:
        levelLock = 1
    if levelLock == 0:
        amountFights += 1
        windowFunction.typeSlow_("Fight Initiated! Get Ready!")
        time.sleep(1)
        battle_()
        areaLevel_()
    else:
        windowFunction.typeSlow_("No enemies left. Progress to continue.")
        time.sleep(1)
        areaLevel_()


def battle_():
    global health, sectionReal
    injured = 0
    Enemy1 = Enemy()
    windowFunction.ClearWindow_
    health = healthInitial + (1**(level * 0.01))
    Enemy1.health = 60 + (20 * (location - 1)) + sectionReal * (2 * (location + 1))
    Enemy1.power = (5 * (location + 1)) + sectionReal
    enemyBufferHp = Enemy1.health
    battleKeep_(Enemy1, injured, enemyBufferHp)
    power = equipped.damage

def battleKeep_(Enemy, injured, enemyBufferHp):
    global listHistory, health, xp, level, selfPower
    power = equipped.damage + selfPower
    win, battleEnding = False, True
    windowFunction.art(1)
    print("""
    
    
    
    """)
    Enemy.enemyStateChoose_()
    print("Enemy Health: ", Enemy.health, "    ", 
          "Enemy Power: ", Enemy.power,"\n\nYour Health:", health,
          "      Your Power:", power, "\n",
          "Choose your action to roll.\n1. Attack\n2. Defend")
    inputAtkLoop = 0 #LOOP FOR THE ATTACK INPUT SYSTEM
    while inputAtkLoop == 0:
        playerAction = input("")
        if playerAction == "1" or playerAction == "2":
            inputAtkLoop = 1
    roll = random.randint(1,6) #ROLL
    print("You have rolled a", roll) #SHOWS ROLL RESULT
    time.sleep(1.5)

    if int(playerAction) == 1:#IF ATTACK
        windowFunction.hit_anim_()
        attack, damage, damageTake = 1, 0, 0
        if Enemy.state == "Attack":
            print("Enemy chooses to attack!")
            time.sleep(1.5)
            if roll == 1:
                damageTake = Enemy.power * 2
                print("You rolled a 1, so the enemy does double damage.")
                damage = random.randint((int(0.5 * power))\
                    ,int((0.7 * power)))
                #SET ATTACK DAMAGE
            elif roll in range(1, 6):
                damageTake = Enemy.power
                damage = random.randint(power,int(power * 1.1))
            elif roll == 6:
                damageTake = Enemy.power
                damage = power * 1.5
                windowFunction.typeVerySlow_("1.5x damage!")
            print("You have dealt", damage, "damage.")
            time.sleep(1.5)
            print("You have lost", damageTake, "health.")
            time.sleep(1.5)
        if Enemy.state == "Defend":
            print("Enemy chooses to defend!")
            time.sleep(1.5)
            match roll:
                case 1:
                    damage = 0
                    windowFunction.typeSlowbattle_("Attack invalidated...")
                    time.sleep(1.5)
                case 2 | 3 | 4 | 5:
                    damage = power * 0.5
                    windowFunction.typeSlowbattle_("Attack damage halved...")
                    time.sleep(1.5)
                case 6:
                    damage = power
                    windowFunction.typeSlowbattle_("You decide to push through"
                    " the shielding and hit at full damage!")
                    time.sleep(1.5)

    elif int(playerAction) == 2: #  
        attack, damage, damageTake = 0, 0, 0
        if Enemy.state == "Attack":
            print("Enemy chooses to attack!")
            time.sleep(1.5)
            match roll:
                case 1:
                    damageTake = 0.5 * Enemy.power
                    print("Defended", (damageTake, "damage"))
                    time.sleep(1.5)
                case 2 | 3 | 4:
                    damageTake = 0.25 * Enemy.power
                    print("Defended", (0.75 * Enemy.power), "damage")
                    time.sleep(1.5)
                case 5:
                    damageTake = 0
                    windowFunction.typeSlow_("Defended all damage")
                    time.sleep(1.5)
                case 6:
                    if health < 100:
                        health = health + (int(health/10))
                    windowFunction.typeSlowbattle_(
                        "You will heal 10% of your health!")
                    time.sleep(0.8)


        elif Enemy.state == "Defend":
            print("Enemy chooses to defend!")
            time.sleep(1.5)
            if health < 100:
                health = health + (int(health / 10))
            windowFunction.typeSlowbattle_("Healed 10% of HP!")
            time.sleep(1.5)
            listHistory.append("def")

    if attack == 1:
        Enemy.health = Enemy.health - damage
    if win == False:
        health = health - damageTake
        if Enemy.health > 0:
            battleKeep_(Enemy, injured, enemyBufferHp)

    if section % 5 != 0:
        if Enemy.health <= 0 and battleEnding == True:
            windowFunction.ClearFrame_()
            windowFunction.typeSlow_("Battle completed!")#SHOW BATTLE COMPLETE
            print("")
            windowFunction.typeVerySlow_("You have earnt...\n")#SHOW HOW MUCH EARNT
            xpEarnt = round((enemyBufferHp / random.randint(2,6)) * 2)
            print(xpEarnt, "XP!")#SHOW XP EARNT
            time.sleep(1.5)#PAUSE
            xpNeeded = ((30**(1 + (level * 0.05))))#CALCULATE XP NEEDED FOR LEVEL UP
            xp = xp + round(xpEarnt)
            battleEnding = False #MAKE SURE THAT THIS MENU DOESNT REPEAT AFTER AREALEVEL ENDS
            while xp >= xpNeeded:#WHILE XP EXCEEDS REQUIRED FOR NEXT LEVEL
                level = level + 1#INCREASE LEVEL
                xp = xp - xpNeeded#REMOVE XP
                windowFunction.typeVerySlow_("You have levelled up!           ")
                print("Level", level - 1, "to", level, "!")
                selfPower += 3#INCREASE POWER BY 3 PER LEVEL
                xp = round(xp)
                time.sleep(3)
            areaLevel_()

def inventory_():
    global equipped
    exited = False
    count = 0
    windowFunction.ClearFrame_()
    for row in inventory:
        count = 0
        for col in row:
            if count == 0:
                nameSelect = "Item:  "
            if count == 1:
                nameSelect = "  Healing:  "
            print(nameSelect, col, end=" ")
            count = count + 1
        print()
    print()

    if RustyBlade.active == True:
        if equipped == RustyBlade:
            print("EQUIPPED")
            power = RustyBlade.damage
        RustyBlade.summary()
        print()
    if CrazyBlade.active == True:
        if equipped == CrazyBlade:
            print("EQUIPPED")
            power = CrazyBlade.damage
        CrazyBlade.summary()
        print()
    print("0: Return to menu  ")
    if RustyBlade.active == True:
        print("1: Equip Rusty Blade  ")
    if CrazyBlade.active == True:
        print("2: Equip Crazy Blade  ")
    while exited == False:
        selection = input("")
        if selection == "0":
            exited = True
            areaLevel_()
        elif selection == "1":
            if RustyBlade.active == True:
                equipped = RustyBlade
                inventory_()
        elif selection == "2":
            if CrazyBlade.active == True:
                equipped = CrazyBlade
                inventory_()


def infoView_(name, job, location, age, weight, birthplace, parent1, parent2):
    #PRINTS OUT THE INFORMATION OF ALLY
    exited = False
    while exited == False:
        selection = input("")
        if selection == "Y":
            windowFunction.ClearWindow_()
            windowFunction.art(7)
            print(name.upper(), "-", job.upper(), "-", location.upper() 
                , "\n", "AGE:", age.upper(), "\n", "WEIGHT:", weight.upper()
                , "\n", "BIRTHPLACE:", birthplace.upper()
                , "\n", "PARENTS:", parent1.upper() + ",", parent2.upper()) 
            exited = True
            input("")
        elif selection == "N":
            exited = True

# MAIN GAME CODE
windowFunction.ClearFrame_()
print("Loading", end='\r') #Print loading, do a carriage return
time.sleep(0.3) #Pause for 0.3 seconds
print("Loading.", end='\r')
time.sleep(0.3)
print("Loading..", end='\r')
time.sleep(0.3)
print("Loading...")
windowFunction.ClearWindow_
windowFunction.BeholdAnimate()

while slopFree == 0:
    slopLength = len(slopList)
    codeLen = len(codeList)
    name = input("                                  "
                 "                     ") #NAME PROMPT
    for i in range(slopLength):
        if slopList[i] in name.lower():
            windowFunction.art(2)
            windowFunction.Text_("BLOODY HELL MATE WHEEEEEEEEEEEEY!!!! "
                                 "COME ON FOOTY LEGENDS!!!!")
            time.sleep(5)
            exit()
    for i in range(codeLen):
        if codeList[i] == "LEVELOFF":
            level_requirement = 0
            slopFree = 1
        elif codeList[i] == "NOGAME":
            area_enabled = 0
            slopFree = 1
windowFunction.Center_() #CENTER NAME PROMPT
exited = False
while exited == False:
    windowFunction.typeSlow_("""Select your text speed.
    1. Slow
    2. Normal
    3. Fast (the intended speed)
    """)
    textSpeed = input()
    match textSpeed:
        case "1":
            windowFunction.textSpeed1 = 0.07
            windowFunction.textSpeedSlow = 0.2
            windowFunction.textSpeedVerySlow = 0.4
            exited = True
        case "2":
            windowFunction.textSpeed1 = 0.035
            windowFunction.textSpeedSlow = 0.15
            windowFunction.textSpeedVerySlow = 0.25
            exited = True
        case "3":
            windowFunction.textSpeed1 = 0.02
            windowFunction.textSpeedSlow = 0.04
            windowFunction.textSpeedVerySlow = 0.08
            exited = True
        case _:
            windowFunction.ClearFrame_()


windowFunction.typeSlow_("Welcome to a perilous journey. "
                         "There will be challenges and triumphs. "
                         "You have seen nothing as of far.") #SLOW TYPE 1 LINE
time.sleep(1)
windowFunction.storySetup_("Mladav Bolen - 1654", 0) 
#SHOW TEXT ON TOP OF IMAGE, PRINT IMAGE BELOW

windowFunction.Text_("you are surrounded by an air of desolateness.\nA faint "
                     "rustle breaks the silence for a second.\nIs it time..? "
                     "I'm probably not going to come out walking but it's "
                     "worth a try.")#SLOWLY PRINT TEXT + INPUT AT END
windowFunction.flashAnim_() #CHANGE SCENE WITH FLASHING ANIMATION
windowFunction.Text_("Oh. What's this then... another one? "
                     "Bloody hell.. they're like vermin.")


windowFunction.ClearWindow_()#CLEARS WINDOW FULLY
windowFunction.storySetup_("Bedroom - Section J", 3)
windowFunction.Text_("""Your heavy eyes slowly begin to lift open as you peer over to your left.
A small, slightly stained envelope is sitting next to your bed, laid hastily on your bedstand.""")
respond_(["yes", "ok", "okay", "sure", "alright", "yeah", "y", "yea"], "The envelope entices you. Do you consume the envelope?   ")
if tick == 1:
    windowFunction.Text_("""Your life goes on as normal. You wake up, eat a meal, and drink some alcohol.
You pick up a small bottle of alcohest and realise that there is a rat dissolved in your drink. 
You decide to drink anyway and you fall asleep.
Your eyes slowly open and a bright flash of fire suddenly appears.
Your life is now over.""")
    input("Enter to exit game.")
    exit()
windowFunction.Text_("""The letter is enclosed with a bright red wax seal, which seemingly leaked into the package.
You take a slight whiff and the stench of wax enters your nostrils.
you begin to sit up and you begin to feel relief that the nightmare was over.
You take another look at the envelope and see a familiar signature""")#USES RAW STRING, WARNING

#WARNING //------------------------------- RAW STRINGS IN THIS IGNORE PEP8 CHARACTER LIMIT FOR CONVENIENCE ---------------------------------//

windowFunction.typeVerySlow_("Signed - Ludvik Novak, with love")
input()


windowFunction.ClearFrame_()
windowFunction.storySetup_("Bedroom - Section J", 3)
windowFunction.Text_("The door to your left swings straight open, and a "
                     "figure stands within the doorway, clenching his arm towards his body.")
print()
windowFunction.Text_("It's too late.\n\nI'm sorry.\n\nWe were too late."
                     "\n\nWhat do we do.. leader?")
respond_()#QUESTION RESPONSE WITH
windowFunction.Text_("""Look. I may be a military manager but I don't think I can do anything. 
I don't think us with our thousands of soldiers can make a dent.
This is your battle.\nThe only one who can fight this fight is you. 
It is written in The Prophecy Of The 3 Heads.
The only one who can truly win is the oprhan of our village..
Everyone here knows that this is you. You need to be the man to save this world. I lend my trust to you for this, the entire city lends their trust.
Fight, not just for me, or you, but for them.
Thank you.""")


windowFunction.ClearFrame_()
windowFunction.storySetup_("Bedroom - Section J", 3)
windowFunction.Text_("You stare at the letter for a bit more, "
                     "and ultimately decide what must be done.")

respond_(["yes", "ok", "okay", "sure", "alright", "yeah", "y", "yea"]
         , "Do you want to journey forward?    ")#QUESTION RESPONSE

if tick == 1:
    windowFunction.Text_("Okay okay.. Here's your sword. "
                         "It's very rusty but it's the best I have currently,"
                         "\nNow here are some apples to eat on the way.")
    areaLevel_()
else:
    windowFunction.Text_("Okay, traitor. Your father would have hoped that"
                         " you could've avenged him but now I\nSee"
                         " that is all for naught. It's sad to do,\n\n\n")
    windowFunction.typeVerySlow_("But it must be done.")
    exit

windowFunction.storySetup_("Greene's Swamp, TOWN", 4)
windowFunction.Text_("""You have been walking down the path for the past 2 hours.
You are now incredibly tired and require rest.""")
windowFunction.Text_("OI YOU, IN HERE!")
windowFunction.Text_("""You suddenly jump from the abrupt message, and then you turn behind
to see a portly, red man standing in your way
THE BLOODY FOOTY'S ON MATE! GET IN!
You hesitate for a moment but you eventually decide to cross the doorway.""")
windowFunction.storySetup_("Barry's Metalworks", 5)
windowFunction.Text_("""Got you, didn't I lad!
I got your back mate.""")
print(name)
windowFunction.Text_("""wasn't it?
Anyways, I know your story, and safe to say our entire village is on board.
Essentially, you're welcome to take anythin', be it a sword or armour, or even some bloody rest.
I know you need some. 
Good luck mate, you'll need it.
Now I'll let you just get some rest in my tavern. Night.""")
windowFunction.storySetup_("Tavern Room C53", 6)
windowFunction.Text_("""You think to yourself about what awaits you. The path, the fights
and everything inbetween.
The thoughts rush through your mind but one stays hidden.
Will you succeed?

You manage to ignore the thoughts and get some good sleep.""")
windowFunction.storySetup_("Barry's Metalworks", 5)
windowFunction.Text_("""You wake up and instantly travel to Barry's hidden store.
You were told the previous night that you could take things but you would rather wait for him.

NEW ALLY DISCOVERED: BARRY GOLDARMS""")
print("VIEW INFO ABOUT ALLY? Y/N")
infoView_("barry goldarms", "master blacksmith", "the old arms",
         "67", "a lot", "hammerfield", "james somerton", "janet silver")
windowFunction.storySetup_("Barry's Metalworks", 5)
windowFunction.Text_("Oi lad, why 'aven't ya grabbed anythin'?\nI'll "
                     "just pick out the lightest one in me collection."
                     "\nHere, a basic, light blade that's suitable for you")
windowFunction.Text_("SWORD OBTAINED!")
print("SWORD NAME:", CrazyBlade.name)
CrazyBlade.active = True
respond_(["yes", "ok", "okay", "sure", "alright", "yeah", "y", "yea"]
         , "Would you like to equip this sword?   ")
if tick == 1:
    equipped = CrazyBlade
    windowFunction.Text_("Sword now equipped")


areaLevel_()
windowFunction.storySetup_("Barry's Metalworks", 5)
windowFunction.Text_("""So, lad, how's it look? Nice, eh?
Give it a swing or two, see how it feels.

Alright. I've kept you 'ere long enough, lad. You better be off on your journey.""")
windowFunction.storySetup_("Forest Path", 8)
windowFunction.Text_("""After walking for miles, 
You decide to think about how life has brought you here.
From stumbling out of your bad and reading a letter to walking down a path of revenge.
You watched as the clouds slowly drifted and pulled out your newly obtained blade.
Feeling the shiny, primed metal on the surface, you began to reminisce about all of the
times you saw soldiers heaving giant swords as a child, and your wish of being able to wield
one of those swords.
It's almost cathartic sitting here, looking at the trees. Seeing the leaves sway.
Seeing the grass follow the wind.

You decide to get up and leave, facing the journey ahead of you.
You detect a slight hint of a smoky smell and you turn to your left.

a small, bearded man stands proudly next to you, carrying a large pot of
boiling stew and a wooden crate of vegetables.""")
windowFunction.Text_("""He looks at you and looks at your shoes, resting his hand
on his chin. He is seemingly trying to figure out who you are""")
windowFunction.Text_("""In a weirdly deep, rumbly voice, the gnome-like man asks a question.
Fancy some sigma stew? Skibidi dop dop dop yes yes?

You look at him in utter bewilderment for a good few seconds.

Oh thank the heavens! A young'un not twisted by the reins of brain squelching content!
Please, take this bowl as a token of my gratificatio- wait, are you the hero?

You grin at him and reach your hand out. He shakes your hand with a shocking amount of force.

He looks at you with a displeased expression after staring at your arms

You realise that I can let you be wanderin' round looking this frail..
take this. 

He hands you a potion simply labelled 'Vitalis'""")
respond_(["yes", "ok", "okay", "sure", "alright", "yeah", "y", "yea"], 
         "Will you drink the potion?    ")
if tick == 1:
    healthInitial = 75
    windowFunction.Text_("""Mate, how does that feel, electrifying, eh?
You'll be able to absorb whatever comes your way now.""")
    windowFunction.typeSlow_("HEALTH NOW PERMANENTLY INCREASED BY 25!")
else:
    windowFunction.Text_("""You decide to turn down the potion

who knows what you missed out on...""")

windowFunction.Text_("""Now, go out there and do what you must! I'll be waitin
on you!""")
areaLevel_()