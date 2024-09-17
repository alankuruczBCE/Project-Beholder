
from shutil import move
import time, windowFunction, random
from tkinter import END
from venv import create
from colorama import Fore


health = 100
level = 1.0
xp = 0
power = 20
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

class Enemy:
    def __init__(self):
        self.health = 100
        self.power = 20
        self.state = "Defend"



    def enemyStateChoose_(self):
        enemyStates = ("Attack", "Defend")
        self.state = random.choice(enemyStates)

def areaLevel_(): #MAIN GAMEPLAY FUNC
    global section
    global location
    global locationName
    global selection #MAKE VARIABLES GLOBAL
    global sectionReal

    windowFunction.ClearFrame_()
    print("Level: " + str(level) + "            " + "XP - " + str(xp)) #PRINT STATS

    if section in range(0,6): #CALCULATE SECTION
        location = 1
    elif section in range(6, 11):
        location = 2

    if location == 1: #FIND LOCATION NAME, SELECT INDEX FOR PRINTING
        locationName = "Granfield"
        index = 0
    elif location == 2:
        locationName = "Granfield - Hills"
        index = 0

    sectionReal = section - ((location-1) * 5) #CALCULATE DISPLAY SECTION
    print(locationName, "-", str(sectionReal)) #PRINT DISPLAY SECTION

    windowFunction.locationArt(index) #PRINT LOCATION ART

    print("1 - Search Location \n2 - View Inventory \n3 - Progress")#PRINT OPTIONS

    selection = int(input("")) #SELECTION DETECTION CODE
    if selection == 1:
        searchArea_()
    elif selection == 2:
        pass
    elif selection == 3:
        section = section + 1
        areaLevel_()
    else:
        areaLevel_()


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
    health = 100
    if location == 1:
        Enemy1.health = 100 + (sectionReal * 4)
        Enemy1.power = 10 + (sectionReal) #SETUP ENEMY STATS
    elif location == 2:
        Enemy1.health = 120 + (sectionReal * 6)
        Enemy1.power = 15 + (sectionReal)
    battleKeep_(Enemy1, injured)

def battleKeep_(Enemy, injured):
    global listHistory
    global health
    global xp
    global level
    win = False
    if location == 1:
        windowFunction.art(1)
    if location == 2:
        windowFunction.art(2)
    print("")
    print("")
    print("")
    print("")
    Enemy.enemyStateChoose_()
    print("Enemy Health: ", Enemy.health, "    ", "Enemy Power: ", Enemy.power)
    print("")
    print("Your Health:", health, "    ", "Your Power: ", power)
    print("Choose your action to roll.\n1. Attack\n2. Defend")
    playerAction = input("")
    roll = random.randint(1,6) #ROLL
    print("You have rolled a", roll)
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
                damage = random.randint((int(0.5 * power)),int((0.7 * power)))#SET ATTACK DAMAG
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
            windowFunction.typeSlow_("Attack damage decreased!")
            time.sleep(1.5)
            if roll == 1:
                damage = 0
                windowFunction.typeSlow_("Attack invalidated...")
                time.sleep(1.5)
            if roll in range(1,5):
                damage = power * 0.5
                windowFunction.typeSlow_("Attack damage halved...")
                time.sleep(1.5)
            if roll == 6:
                damage = power
                windowFunction.typeSlow_("You decide to push through the shielding and hit at full damage!")
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
                print_("Defended", (damageTake, "damage"))
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
                windowFunction.typeVerySlow_("You will heal 10% of your health!")
                time.sleep(0.8)
            listHistory.append("atk")
        elif Enemy.state == "Defend":
            print("Enemy chooses to defend!")
            time.sleep(1.5)
            if health < 100:
                health = health + (int(health / 10))
            windowFunction.typeSlow_("Healed 10% of HP!")
            time.sleep(1.5)
            listHistory.append("def")

    if len(listHistory) == 4:
        listHistory.pop(3)
    if listHistory.count("atk") == 3:
        injured = 1
        windowFunction.typeSlow_("You have been injured! You now take 1.5x damage until the end of the battle!")
        time.sleep(1.5)
    if injured == 1:
        damageTake = damageTake * 1.5
    if attack == 1:
        Enemy.health = Enemy.health - damage
    if win == False:
        health = health - damageTake
        if Enemy.health > 0:
            battleKeep_(Enemy, injured)
    if Enemy.health <= 0:
        windowFunction.ClearFrame_()
        windowFunction.typeSlow_("Battle completed!")
        print("")
        windowFunction.typeVerySlow_("You have earnt...")
        xpEarnt = (Enemy.health / 4)
        print(xpEarnt)
        time.sleep(1.5)
        xpNeeded = ((100**(level * 0.5)))
        xp = xp + xpEarnt
        while xp >= xpNeeded:
            level = level + 1
            xp = xp - xpNeeded
            windowFunction.typeVerySlow_("You have levelled up!")
            print("Level", level - 1, "to", level, "!")
            time.sleep(3)
        areaLevel_()




areaLevel_() #INITALISE MAIN GAMEPLAY MENU
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

name = input("                                                       ") #NAME PROMPT
windowFunction.Center_() #CENTER NAME PROMPT
windowFunction.typeSlow_("Welcome to a perilous journey. There will be challenges and triumphs. You have seen nothing as of far.") #SLOW TYPE 1 LINE
time.sleep(1)
windowFunction.storySetup_("Mladav Bolen - 1654", 0) #SHOW TEXT ON TOP OF IMAGE, PRINT IMAGE BELOW
windowFunction.Text_("you are surrounded by an air of desolateness. (ENTER to continue)")
windowFunction.Text_("A faint rustle breaks the silence for a second.")
windowFunction.Text_("Is it time..? I'm probably not going to come out walking but it's worth a try.")
windowFunction.flashAnim_() #CHANGE SCENE WITH FLASHING ANIMATION
windowFunction.Text_("Oh. What's this then... another one? Bloody hell.. they're like vermin.")
windowFunction.Center_()
areaLevel_() #INITALISE MAIN GAMEPLAY MENU
