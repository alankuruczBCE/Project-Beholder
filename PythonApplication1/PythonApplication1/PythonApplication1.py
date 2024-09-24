
from ast import Constant
from cgitb import text
from operator import eq
from pickle import APPEND
from shutil import move
import time, windowFunction, random
from urllib import response
from tkinter.font import names
from turtle import clear
from tkinter import END
from venv import create


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
xpNeeded = 100
inventory = [["Apple", 5],["Apple", 5]]
apple = ["Apple", 5]
slopList = ["john pork", "skibidi", "toilet", "soy", "wojak", "baby gronk", "friend", "kris", "senan", "roblox", "homestuck", "speed", "fanum", "brainrot", "camera", "mario", "chud", "chad", "costco", "among us", "sus", "mewing", "sigma", "hawk", "tuah", "haircut"]
slopFree = 0
sectionPause = 0
tick = 0


def respond_(responseWords):
    global tick
    print()
    print()
    response = input("What do you respond with?    ")
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
        print(self.index, ":", self.name, "  Damage: ", str(self.damage), "\nDescription:  ", self.description)

RustyBlade = Weapon(1,"Rusty Training Blade", 9999, "It may or may not do the job. I don't think it will but it's up to you.", True)
CrazyBlade = Weapon(2,"Scary Blade!", 30, "BOOOO!", False)
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

    windowFunction.ClearFrame_()
    print("Level: " + str(level) + "            " + "XP - " + str(xp)) #PRINT STATS
    if sectionPause == 1:
        sectionPause = 0
        section += 1
        return
        


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

    sectionReal = section - ((location-1) * 5) #CALCULATE DISPLAY SECTION
    print(locationName, "-", str(sectionReal)) #PRINT DISPLAY SECTION

    windowFunction.locationArt(index) #PRINT LOCATION ART

    print("1 - Search Location \n2 - View Inventory \n3 - Progress \n4- Add an Apple")#PRINT OPTIONS

    selection = int(input("")) #SELECTION DETECTION CODE
    if selection == 1:
        searchArea_()
    elif selection == 2:
        inventory_()
    elif selection == 3:
        if section == 5:
            sectionPause = 1
            return
        if section == 10:
            sectionPause = 1
            return
        section = section + 1
        areaLevel_()
    elif selection == 4:
        addItem_(inventory, apple)
        areaLevel_()
    else:
        areaLevel_()

def addItem_(listicle,element):
    listicle.append(element)
    return 1


def searchArea_():
    global randomEnemy
    global xp
    
    randomEnemy = random.randint(1,2)
    if randomEnemy == 1:
        print("Enemy found!")
        time.sleep(1)
        battle_()
        areaLevel_()
    else:
        print("no enemy")
        time.sleep(1)
        areaLevel_()


def battle_():
    global health
    global sectionReal
    injured = 0
    Enemy1 = Enemy()
    windowFunction.ClearWindow_
    health = 50 + (1**(level * 0.01))
    if location == 1:
        Enemy1.health = 60 + (sectionReal * 4)
        Enemy1.power = 10 + (sectionReal) #SETUP ENEMY STATS
    elif location == 2:
        Enemy1.health = 80 + (sectionReal * 6)
        Enemy1.power = 15 + (sectionReal)
    enemyBufferHp = Enemy1.health
    battleKeep_(Enemy1, injured, enemyBufferHp)

def battleKeep_(Enemy, injured, enemyBufferHp):
    global listHistory
    global health
    global xp
    global level
    win = False
    battleEnding = True
    if location == 1:
        windowFunction.art(1)
    if location == 2:
        windowFunction.art(1)
    print("")
    print("")
    print("")
    print("")
    Enemy.enemyStateChoose_()
    print("Enemy Health: ", Enemy.health, "    ", "Enemy Power: ", Enemy.power)
    print("")
    print("Your Health:", health, "    ", "Your Power: ", power)
    print("Choose your action to roll.\n1. Attack\n2. Defend")
    inputAtkLoop = 0 #LOOP FOR THE ATTACK INPUT SYSTEM
    while inputAtkLoop == 0:
        playerAction = input("")
        if playerAction == "1" or playerAction == "2":
            inputAtkLoop = 1
    roll = random.randint(1,6) #ROLL
    print("You have rolled a", roll) #SHOWS ROLL RESULT
    time.sleep(1.5)
    if int(playerAction) == 1:#IF ATTACK
        attack = 1
        damage = 10.0
        damageTake = 0
        if Enemy.state == "Attack":
            print("Enemy chooses to attack!")
            time.sleep(1.5)
            if roll == 1:
                damageTake = Enemy.power * 2
                print("You rolled a 1, so the enemy does double damage.")
                damage = random.randint((int(0.5 * power)),int((0.7 * power)))#SET ATTACK DAMAGE
            elif roll in range(1, 5):
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
            time.sleep(1)
            windowFunction.typeSlowbattle_("Attack damage decreased!")
            time.sleep(1.5)
            if roll == 1:
                damage = 0
                windowFunction.typeSlowbattle_("Attack invalidated...")
                time.sleep(1.5)
            if roll in range(1,5):
                damage = power * 0.5
                windowFunction.typeSlowbattle_("Attack damage halved...")
                time.sleep(1.5)
            if roll == 6:
                damage = power
                windowFunction.typeSlowbattle_("You decide to push through the shielding and hit at full damage!")
                time.sleep(1.5)


    elif int(playerAction) == 2:
        attack = 0
        damage = 0
        damageTake = 0
        if Enemy.state == "Attack":
            print("Enemy chooses to attack!")
            time.sleep(1.5)
            if roll == 1:
                damageTake = 0.5 * Enemy.power
                print("Defended", (damageTake, "damage"))
                time.sleep(1.5)
            elif roll in range(1, 4):
                damageTake = 0.25 * Enemy.power
                print("Defended", (0.75 * Enemy.power), "damage")
                time.sleep(1.5)
            elif roll == 5:
                damageTake = 0
                windowFunction.typeSlow_("Defended all damage")
                time.sleep(1.5)
            elif roll == 6:
                if health < 100:
                    health = health + (int(health/10))
                windowFunction.typeSlowbattle_("You will heal 10% of your health!")
                time.sleep(0.8)
            listHistory.append("atk")
        elif Enemy.state == "Defend":
            print("Enemy chooses to defend!")
            time.sleep(1.5)
            if health < 100:
                health = health + (int(health / 10))
            windowFunction.typeSlowbattle_("Healed 10% of HP!")
            time.sleep(1.5)
            listHistory.append("def")

    if len(listHistory) == 4:
        listHistory.pop(3)
    if listHistory.count("atk") == 3:
        injured = 1
        windowFunction.typeSlowbattle_("You have been injured! You now take 1.5x damage until the end of the battle!")
        time.sleep(1.5)
    if injured == 1:
        damageTake = damageTake * 1.5
    if attack == 1:
        Enemy.health = Enemy.health - damage
    if win == False:
        health = health - damageTake
        if Enemy.health > 0:
            battleKeep_(Enemy, injured, enemyBufferHp)

    if section != 5 or section != 10:
        if Enemy.health <= 0 and battleEnding == True:
            windowFunction.ClearFrame_()
            windowFunction.typeSlow_("Battle completed!")
            print("")
            windowFunction.typeVerySlow_("You have earnt...\n")
            xpEarnt = (enemyBufferHp / 4)
            print(xpEarnt, "XP!")
            time.sleep(1.5)
            xpNeeded = ((100**(1 + (level * 0.05))))
            xp = xp + xpEarnt
            battleEnding = False
            while xp >= xpNeeded:
                level = level + 1
                xp = xp - xpNeeded
                windowFunction.typeVerySlow_("You have levelled up!")
                print("Level", level - 1, "to", level, "!")
                time.sleep(3)
            areaLevel_()

def inventory_():
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
    print("0: Return to menu")
    selection = input("")
    if selection == "0":
        areaLevel_()


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
    name = input("                                                       ") #NAME PROMPT
    for i in range(slopLength):
        if slopList[i] in name.lower():
            windowFunction.art(2)
            windowFunction.Text_("BLOODY HELL MATE WHEEEEEEEEEEEEY!!!! COME ON FOOTY LEGENDS!!!!")
            time.sleep(5)
            exit()
        else:
            slopFree = 1


windowFunction.Center_() #CENTER NAME PROMPT
windowFunction.typeSlow_("Welcome to a perilous journey. There will be challenges and triumphs. You have seen nothing as of far.") #SLOW TYPE 1 LINE
time.sleep(1)
windowFunction.storySetup_("Mladav Bolen - 1654", 0) #SHOW TEXT ON TOP OF IMAGE, PRINT IMAGE BELOW
windowFunction.Text_("you are surrounded by an air of desolateness.\nA faint rustle breaks the silence for a second.\nIs it time..? I'm probably not going to come out walking but it's worth a try.")
windowFunction.flashAnim_() #CHANGE SCENE WITH FLASHING ANIMATION
windowFunction.Text_("Oh. What's this then... another one? Bloody hell.. they're like vermin.")
windowFunction.Center_()
time.sleep(1.5)


windowFunction.ClearWindow_()
windowFunction.storySetup_("Bedroom - Section J", 3)
windowFunction.Text_("Your heavy eyes slowly begin to lift open as you peer over to your left.\nA small, slightly stained envelope is sitting next to your bed, laid hastily on your bedstand.\nThe letter is enclosed with a bright red wax seal, which seemingly leaked into the package.\nYou take a slight whiff and the stench of wax enters your nostrils.\nyou begin to sit up and you begin to feel relief that the nightmare was over.\nYou take another look at the envelope and see a familiar signature")
windowFunction.typeVerySlow_("Signed - Ludvik Novak, with love")
input()


windowFunction.ClearFrame_()
windowFunction.storySetup_("Bedroom - Section J", 3)
windowFunction.Text_("The door to your left swings straight open, and a figure stands within the doorway, clenching his arm towards his body.")
print()
windowFunction.Text_("It's too late.\n\nI'm sorry.\n\nWe were too late.\n\nWhat do we do.. leader?")
respond_(["WHEEEEEEY"])
windowFunction.Text_("Look. I may be a military manager but I don't think I can do anything. \nI don't think us with our thousands of soldiers can make a dent.\nThis is your battle.\nThe only one who can fight this fight is you. \nIt is written in The Prophecy Of The 3 Heads.\nThe only one who can truly win is the oprhan of our village..\nEveryone here knows that this is you. You need to be the man to save this world. I lend my trust to you for this, the entire city lends their trust.\nFight, not just for me, or you, but for them.\nThank you.")


windowFunction.ClearFrame_()
windowFunction.storySetup_("Bedroom - Section J", 3)
windowFunction.Text_("You stare at the letter for a bit more, and ultimately decide what must be done. Do you want to?")

respond_(["yes", "ok", "okay", "sure", "alright", "yeah", "y"])

if tick == 1:
    windowFunction.Text_("Okay okay.. Here's your sword .It's very rusty but it's the best I have currently,\nNow here are some apples to eat on the way.")
    areaLevel_()
else:
    windowFunction.Text_("Okay, traitor. Your father would have hoped that you could've avenged him but now I\nSee that is all for naught. It's sad to do,\n\n\n")
    windowFunction.typeVerySlow_("But it must be done.")
    exit