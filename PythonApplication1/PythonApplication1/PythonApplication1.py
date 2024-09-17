
from shutil import move
import time, windowFunction, random
from tkinter import END
from venv import create
import random



health = 100
level = 1
xp = 10
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
class Enemy:
    def __init__(self, health, power, state):
        self.health = enemyHealth
        self.power = enemyPower
        self.state = enemyState


def createEnemy_():
    Enemy1 = Enemy(enemyHealth, enemyPower, enemyState)

def deleteEnemy_():
    del Enemy

def enemyStateChoose_():
    enemyStates = ("Attack", "Defend")
    Enemy.state = random.choice(enemyStates)

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
    global xp
    global enemy
    windowFunction.ClearWindow_
    health = 100
    createEnemy_()
    enemyStateChoose_()
    if location == 1:
        Enemy.health = 100 + (sectionReal * 4)
        Enemy.power = 10 + (sectionReal) #SETUP ENEMY STATS
    elif location == 2:
        Enemy.health = 120 + (sectionReal * 6)
        Enemy.power = 15 + (sectionReal)
    battleKeep_()

def battleKeep_():
    global listHistory
    global health
    global xp
    win = False
    windowFunction.ClearWindow_()
    print("Enemy Health: ", Enemy.health, "    ", "Enemy Power: ", Enemy.power)
    playerAction = input("Choose your action to roll.\n1. Attack\n2. Defend")
    roll = random.randint(0,6) #ROLL
    if int(playerAction) == 1:#IF ATTACK
        damage = 10.0
        damageTake = 1.0
        if roll == 1:
            damageTake = 0 #DONT TAKE DAMAGE
            damage = random.randint((int(0.5 * power)),int((0.7 * power)))#SET ATTACK DAMAG
        elif roll in range(1, 5):
            damage = random.randint(power,int(power * 1.1))
        elif roll == 6:
            damage = power * 1.5

        listHistory.append("atk") #ADD ATTACK TO HISTORY
    elif int(playerAction) == 2:
        damage = 0
        if Enemy.state == "Attack":
            if roll == 1:
                damageTake = 0.5 * Enemy.power
                print("Defended", (damageTake, "damage"))
            elif roll in range(1, 4):
                damageTake = 0.25 * Enemy.power
                print("Defended", (0.75 * Enemy.power), "damage")
            elif roll == 5:
                damageTake = 0
                print("Defended all damage")
            elif roll == 6:
                health = health + (health/10)
        elif Enemy.state == "Defend":
            health = health + (health / 10)


    Enemy.health = Enemy.health - damage
    if Enemy.health <= 0:
        win = True
        print("Won")
        time.wait(1)
        areaLevel_()
    if win == False:
        health = health - damageTake
        if health <= 0:
            END
    else:
        battleKeep_()




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
