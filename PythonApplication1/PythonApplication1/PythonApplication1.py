#-----------------------------------IMPORTS----------------------------------¦
from genericpath import isfile
import time
import windowFunction
import random
import os

#-----------------------------------VARIABLES--------------------------------¦
health = 50
level = 1.0
xp = 0
power = 0
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
codeList = ["LEVELOFF"]
tick = 0
selfPower = 0
healthBoost = 0
healthInitial = 50
losses = 0
#-------------------------------PARAMETERS-----------------------------------¦
level_requirement = 1
slopFree = 0
levelLock = 0
sectionPause = 0
bossBattle = 0
bossBeat = 0
bossLoss = 0
mysteryFight = 0

# FUNCTION DECLARATIONS
def save_apply_():
    global losses
    saveFile = open("saveFile.txt", "w")
    saveFile.write(str(losses))#LINE 1 LOSSES
    saveFile.close()


def respond_(responseWords = "test", responseText = "What do you respond " 
             "with?    "):
    responseValidated = 0
    global tick
    print()
    print()
    while responseValidated == 0:
        response = input(responseText)
        if response != "":
            responseValidated = 1
    tick = 0
    print()
    print()
    responseLength = len(responseWords)
    for i in range(responseLength):
        if responseWords[i] in response.lower():
            tick = 1
    return response


class Weapon:
    def __init__(self, name):
        self.name = name
        
        if name == "Training Basher":
            self.index = 1
            self.damage = 30
            self.description = """It may or may not do the job. 
            I don't think it will but it's up to you."""
            self.active = True
        elif name == "Light Steel":
            self.index = 2
            self.damage = 80
            self.description = "It's basic, it hurts to get hit by."
            self.active = False


    def summary(self):
        print(self.index, ":", self.name, "  Damage: ", str(self.damage), 
              "\nDescription:  ", self.description)

Blade1 = Weapon("Training Basher")
Blade2 = Weapon("Light Steel")
equipped = Blade1
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
    global bossBattle
    xpNeeded = (30 + (level * 5))
    windowFunction.ClearFrame_()
    print("Level: " + str(level) + "            " + "XP - " + str(xp) + 
            "             " + "XP until level", str(int(level) + 1)
            + " -", str(round(xpNeeded) - xp)) #PRINT STATS
        

    if section in range(0,6): #CALCULATE SECTION
        location = 1
    elif section in range(6, 11):
        location = 2
    elif section in range(11, 16):
        location = 3
    elif section in range(16, 21):
        location = 4
    elif section in range(21, 26):
        location = 5
    elif section == 26:
        location = 6
        bossBattle = 1
    elif section in range(31, 36):
        location = 7

    if section == 36:
        mysteryFight = 1

    sectionReal = section - ((location - 1) * 5)##NOTE -------------------------------------------------------------------- MAKE THE SECTION 31 WHEN BOSS DIES
    if location == 1: #FIND LOCATION NAME, SELECT INDEX FOR PRINTING
        locationName = "Granfield"
        index = 0
    elif location == 2:
        locationName = "Granfield - Hills"
        index = 1
    elif location == 3:
        locationNmae = "Vesenid"
        index = 2
    elif location == 4:
        locationName = "No Man's Forest"
        index = 3
    elif location == 5:
        locationName = "Mlavav Bolen"
        index = 4
    elif location == 6:
        locationName = "DOOMSDAY"
        index = 5
    elif location == 7:
        locationName = "Field Of Dreams"
        index = 6

    print(locationName, "-", str(sectionReal)) #PRINT DISPLAY SECTION
    windowFunction.locationArt(index) #PRINT LOCATION ART

    if bossBattle == 0:
        if level - 1 >= section:
            print("1 - Fight \n2 - View Inventory \n3 - Progress \n"
                    "4- Add an Apple")#PRINT OPTIONS
        else:
            print("1 - Fight \n2 - View Inventory \n3 - "
                    "(NEED TO LEVEL UP TO PROGRESS) \n4- Add an Apple")
                    #PRINT OPTIONS
    else:
        print("1 - Fight the boss.")

    selection = input("") #SELECTION DETECTION CODE
    if selection == "1":
        searchArea_()
    if bossBattle == 0:
        if selection == "2":
            inventory_()
        elif selection == "3":
            levelLock = 0
            if section % 5 == 0:
                section = section + 1
                return
            elif level - 1 >= section:
                section = section + 1
                areaLevel_()
    else:
        areaLevel_()



def addItem_(listicle,element):
    listicle.append(element)
    return 1


def searchArea_():
    windowFunction.typeSlow_("Fight Initiated! Get Ready!")
    time.sleep(1)
    battle_()


def battle_():     #INITIALISE BATTLE
    global health
    global bossBattle
    global sectionReal
    Enemy1 = Enemy()#CREATE ENEMY
    windowFunction.ClearWindow_() #CLEAR THE WINDOW
    health = healthInitial + (1**(level * 0.01))#SET PLAYER HEALTH
    if bossBattle == 0:
        Enemy1.health = 60 + (20 * (location - 1)) + \
            sectionReal * (2 * (location + 1))
    else:
        Enemy1.health = 300
    #SET ENEMY HEALTH
    if bossBattle == 0:
        Enemy1.power = (5 * (location + 1)) + sectionReal#SET ENEMY POWER
    else:
        Enemy1.power = 60
    enemyBufferHp = Enemy1.health#SET ENEMY MAX HEALTH
    battleKeep_(Enemy1, enemyBufferHp)#ENTER MAIN BATTLE

def battleKeep_(Enemy, enemyBufferHp):#MAIN BATTLE CODE
    global listHistory
    global health
    global xp
    global level
    global selfPower
    global healthBoost
    global levelMenu
    global xpNeeded
    global bossBattle
    power = equipped.damage + selfPower#SET PLAYER POWER
    win = False 
    levelMenu = False
    if bossBattle == 0:
        windowFunction.art(1)#PRINT BATTLE ARTT
    else:
        windowFunction.locationArt(5)
    print("""
    
    """)#CREATE SPACES
    Enemy.enemyStateChoose_()#ENEMY PICKS STATE
    if bossBattle == 0:
        print("Enemy Health: ", Enemy.health, "    ", 
              "Enemy Power: ", Enemy.power,"\n\nYour Health:", health,
              "      Your Power:", power, "\n",
              "Choose your action to roll.\n1. Attack\n2. Defend")
    else:
        print("Baron's Health: ", Enemy.health, "    ", 
              "Baron's Power: ", Enemy.power,"\n\nYour Health:", health,
              "      Your Power:", power, "\n",
              "Choose your action to roll.\n1. Attack\n2. Defend")
            #PRINT STATS FOR BATTLE
    inputAtkLoop = 0 #LOOP FOR THE ATTACK INPUT SYSTEM
    while inputAtkLoop == 0:
        playerAction = input("")
        if playerAction == "1" or playerAction == "2":
            inputAtkLoop = 1#BREAK LOOP IF CORRECT ACTION PICKED
    roll = random.randint(1,6) #ROLL
    print("You have rolled a", roll) #SHOWS ROLL RESULT
    time.sleep(1.5)

    if int(playerAction) == 1:#IF ATTACK
        windowFunction.hit_anim_()#PLAY HIT ANIMATION
        attack = 1#ATTACKING IS SELECTED
        damage = 0#RESET DAMAGE GIVEN + TAKEN
        damageTake = 0
        if Enemy.state == "Attack":#IF ENEMY IS ATTACKING
            print("Enemy chooses to attack!")
            time.sleep(1.5)
            match roll:#SWITCH STATEMENT FOR ROLLING
                case 1:
                    damageTake = Enemy.power * 2#ENEMY DOUBLES DAMAGE
                    print("You rolled a 1, so the enemy does double damage.")
                    damage = random.randint((int(0.5 * power))\
                        ,int((0.7 * power))) #SET DAMAGE
                case 2 | 3 | 4 | 5:#IF ROLL BETWEEN 2 AND 5
                    damageTake = Enemy.power#DAMAGE TAKEN NORMAL
                    damage = random.randint(power,int(power * 1.1))
                    #DAMAGE AMOUNT SELECTED
                case 6:
                    damageTake = Enemy.power
                    damage = power * 1.5
                    windowFunction.typeVerySlow_("1.5x damage!")
            print("You have dealt", damage, "damage.")#SHOW DAMAGE DEALT
            time.sleep(1.5)
            print("You have lost", damageTake, "health.")#SHOW HEALTH LOST
            time.sleep(1.5)
        if Enemy.state == "Defend":#IF ENEMY DEFENDING
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
            battleKeep_(Enemy, enemyBufferHp)

    if Enemy.health <= 0 and bossBattle == 0:
        Enemy.health = 1
        windowFunction.ClearFrame_()
        windowFunction.typeSlow_("Battle completed!")#SHOW BATTLE COMPLETE
        print("")
        windowFunction.typeVerySlow_("You have earnt...\n")#SHOW HOW MUCH EARNT
        xpEarnt = round((enemyBufferHp / random.randint(3,6)) * 2)
        print(xpEarnt, "XP!")#SHOW XP EARNT
        time.sleep(1.5)#PAUSE
        xpNeeded = 30 + (level * 5)#CALCULATE XP NEEDED FOR LEVEL UP
        xp = xp + round(xpEarnt)
        #xp = xp + round(xpEarnt)
        if xp >= xpNeeded:
            xp_menu_()
        else:
            time.sleep(3)
        areaLevel_()
    elif Enemy.health <= 0 and bossBattle == 1:
        bossBeat = 1
        return

    if health <= 0:
        losses += 1
        save_apply_()
        areaLevel_()
    elif health <= 0 and bossBattle == 1:
        bossLoss = 1
        return


def xp_menu_():
    global xp
    global level
    global xpNeeded
    global healthInitial
    global selfPower
    level = level + 1#INCREASE LEVEL
    xp = xp - xpNeeded#REMOVE XP
    windowFunction.typeVerySlow_("You have levelled up!           ")
    print("Level", level - 1, "to", level, "!")
    selfPower += 2#INCREASE POWER BY 3 PER LEVEL
    healthInitial += 3
    xp = round(xp)
    if xp >= xpNeeded:
        xp_menu_()



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

    if Blade1.active == True:
        if equipped == Blade1:
            print("EQUIPPED")
            power = Blade1.damage
        Blade1.summary()
        print()
    if Blade2.active == True:
        if equipped == Blade2:
            print("EQUIPPED")
            power = Blade2.damage
        Blade2.summary()
        print()
    print("0: Return to menu  ")
    if Blade1.active == True:
        print("1: Equip Rusty Blade  ")
    if Blade2.active == True:
        print("2: Equip Crazy Blade  ")
    while exited == False:
        selection = input("")
        if selection == "0":
            exited = True
            areaLevel_()
        elif selection == "1":
            if Blade1.active == True:
                equipped = Blade1
                inventory_()
        elif selection == "2":
            if Blade2.active == True:
                equipped = Blade2
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

# --------------------------------------------------------------MAIN GAME CODE

    #make file
save_apply_()
windowFunction.ClearFrame_()
print("Loading", end='\r') #Print loading, do a carriage return
time.sleep(0.3) #Pause for 0.3 seconds
print("Loading.", end='\r')
time.sleep(0.3)
print("Loading..", end='\r')
time.sleep(0.3)
print("Loading...")
windowFunction.ClearWindow_
saveFile = open("saveFile.txt", "r")
windowFunction.BeholdAnimate(saveFile)
saveFile.close()
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
        if name == "LEVELOFF":
            level_requirement = 0
            slopFree = 1
        else:
            level_requirement = 1
            area_enabled = 1
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
    
windowFunction.typeSlow_("""Welcome to a perilous journey.
    There will be challenges and triumphs. 
    You have seen nothing as of far.""") #SLOW TYPE 1 LINE
time.sleep(1)
windowFunction.storySetup_("Mladav Bolen - 1654", 0) 
#SHOW TEXT ON TOP OF IMAGE, PRINT IMAGE BELOW
windowFunction.Text_("""    you are surrounded by an air of desolateness.
    A faint rustle breaks the silence for a second.
    Is it time..? 
    I'm probably not going to come out walking but it's 
    worth a try.""")#SLOWLY PRINT TEXT
windowFunction.flashAnim_() #CHANGE SCENE WITH FLASHING ANIMATION
windowFunction.Text_("  Oh. What's this then... another one? "
                        "   Bloody hell.. they're like vermin.")


windowFunction.ClearWindow_()#CLEARS WINDOW FULLY
windowFunction.storySetup_("Bedroom - Velograd Heights", 3)
windowFunction.Text_("""    Your heavy eyes slowly begin to lift 
    open as you peer over to your left.
    A small, slightly stained envelope is sitting 
    next to your bed, laid hastily on your bedstand.""")
respond_(["yes", "ok", "okay", "sure", "alright", "yeah", "y", "yea"], \
    "   The envelope entices you. Do you consume the envelope?   ")
if tick == 1:
    windowFunction.Text_("""    Your life goes on as normal. 
    You wake up, eat a meal, and drink some alcohol.
    You pick up a small bottle of alcohest and realise 
    that there is a rat dissolved in your drink. 
    You decide to drink anyway and you fall asleep.
    Your eyes slowly open and a bright flash of fire suddenly appears.
    Your life is now over.""")
    input("         Enter to exit game.")
    exit()
windowFunction.Text_("""    The letter is enclosed with a 
    bright red wax seal, which seemingly leaked into the package.
    You take a slight whiff and the stench of wax enters your nostrils.
    you begin to sit up and you begin to feel 
    relief that the nightmare was over.
    You take another look at the envelope 
    and see a familiar signature""")#USES RAW STRING, WARNING



windowFunction.typeVerySlow_("  Signed - Ludvik Novak, with love")
input()


windowFunction.ClearFrame_()
windowFunction.storySetup_("Bedroom - Velograd Heights", 3)
windowFunction.Text_("""    The door to your left swings straight open, and a 
    figure stands within the doorway, clenching his arm towards his body.""")
print()
windowFunction.Text_("""    It's too late.      
    I'm sorry.     
    We were too late.     
    \n\nWhat do we do.. leader?""")
respond_()#QUESTION RESPONSE WITH
windowFunction.Text_("""    Look. I may be a fighter, 
    but I don't think I can do anything. 
    I don't think us with our thousands of soldiers can make a dent.
    This is your battle.
    The only one who can fight this fight is you. 
    It is written in The Prophecy Of The 3 Heads.
    The only one who can truly win is the oprhan of our village..
    Everyone here knows that this is you. 
    You need to be the man to save this world. 
    I lend my trust to you for this, the entire city lends their trust.
    Fight, not just for me, or you, but for them.
    Thank you.""")


windowFunction.ClearFrame_()
windowFunction.storySetup_("Bedroom - Velograd Heights", 3)
windowFunction.Text_("""    You stare at the letter for a bit more,
    and ultimately decide what must be done.""")

respond_(["yes", "ok", "okay", "sure", "alright", "yeah", "y", "yea"]
            , "    Do you want to journey forward?    ")#QUESTION RESPONSE

if tick == 1:
    windowFunction.Text_("""    Okay okay.. Here's your sword. 
    It's very rusty but it's the best I have currently, 
    Now here are some apples to eat on the way.""")
    areaLevel_()#//--------------- ACT 1 - BEGINNING -----------------------//
else:
    windowFunction.Text_("""    Okay, traitor. 
    Your father would have hoped that 
    you could've avenged him but now I see 
    that is all for naught. It's sad to do.""")
    windowFunction.typeVerySlow_("  But it must be done.")
    exit

windowFunction.storySetup_("Greene's Swamp, TOWN", 4)
windowFunction.Text_("""    You have been walking down 
    the path for the past 2 hours.
    You are now incredibly tired and require rest.""")
windowFunction.Text_("  OI YOU, IN HERE!")
windowFunction.Text_("""    You suddenly jump from the abrupt message, 
    and then you turn behind
    to see a portly, red man standing in your way
    THE BLOODY FOOTY'S ON MATE! GET IN!
    You hesitate for a moment but you 
    eventually decide to cross the doorway.""")
windowFunction.storySetup_("Barry's Metalworks", 5)
windowFunction.Text_("""    Got you, didn't I lad!
    I got your back mate""")
print(name)
windowFunction.Text_("""    wasn't it?
    Anyways, I know your story, and safe to say 
    our entire village is on board.
    Essentially, you're welcome to take anythin', 
    be it a sword or armour, or even some bloody rest.
    I know you need some. 
    Good luck mate, you'll need it.
    Now I'll let you just get some rest in my tavern. Night.""")
windowFunction.storySetup_("Tavern Room C53", 6)
windowFunction.Text_("""    You think to yourself about what awaits you.
    The path, the fights and everything inbetween.
    The thoughts rush through your mind but one stays hidden.
    Will you succeed?

    You manage to ignore the thoughts and get some good sleep.""")
windowFunction.storySetup_("Barry's Metalworks", 5)
windowFunction.Text_("""    You wake up and walk briskly 
    to Barry's Metalworks.
    You were told the previous night that you could take things,
    but you would rather wait for him.

NEW ALLY DISCOVERED: BARRY GOLDARMS""")
print("VIEW INFO ABOUT ALLY? Y/N")
infoView_("barry goldarms", "master blacksmith", "the old arms",
            "67", "a lot", "hammerfield", "james somerton", "janet silver")
windowFunction.storySetup_("Barry's Metalworks", 5)
windowFunction.Text_("""    Oi lad, why 'aven't ya grabbed anythin'? I'll 
    just pick out the lightest one in me collection. 
    Here, a basic, light blade that's suitable for you""")
windowFunction.Text_("SWORD OBTAINED!")
print("SWORD NAME:", Blade2.name)
Blade2.active = True
respond_(["yes", "ok", "okay", "sure", "alright", "yeah", "y", "yea"]
            , "    Would you like to equip this sword?   ")
if tick == 1:
    equipped = Blade2
    windowFunction.Text_("Sword now equipped")


areaLevel_()#//---------------------ACT 2 - A RANDOM GIFT-------------------//
windowFunction.storySetup_("Barry's Metalworks", 5)
windowFunction.Text_("""    So, lad, how's it look? Nice, eh?
    Give it a swing or two, see how it feels.

    Alright. I've kept you 'ere long enough, lad. 
    You better be off on your journey.""")
windowFunction.storySetup_("Forest Path", 8)

windowFunction.Text_("""    After walking for miles, 
    You decide to think about how life has brought you here.
    From stumbling out of your bed 
    to reading a letter 
    to walking down a path of revenge.
    You watched as the clouds slowly drifted 
    and pulled out your newly obtained blade.
    Feeling the shiny, primed metal on the surface, 
    you began to reminisce about all of the
    times you saw soldiers heaving giant swords as a child, 
    and your wish of being able to wield one of those swords.
    It's almost cathartic sitting here, looking at the trees. 
    Seeing the leaves sway.
    Seeing the grass follow the wind.

    You decide to get up and leave, facing the journey ahead of you.
    You detect a slight hint of a smoky smell and you turn to your left.

    a small, bearded man stands proudly next to you, carrying a large pot of
    boiling stew and a wooden crate of vegetables.""")

windowFunction.Text_("""    He looks at you and looks at your shoes, 
    resting his hand on his chin. 
    He is seemingly trying to figure out who you are""")

windowFunction.Text_("""    In a weirdly deep, rumbly voice, 
    the gnome-like man asks a question.
    Fancy some sigma stew? Skibidi dop dop dop yes yes?

    You look at him in utter bewilderment for a good few seconds.

    Oh thank the heavens! 
    A young'un not twisted by the reins of brain squelching content!
    Please, take this bowl as a token of my gratificatio- 
    wait, are you the hero?

    You grin at him and reach your hand out. 
    He shakes your hand with a shocking amount of force.

    He looks at you with a displeased expression after staring at your arms

    You realise that I can't let you be wanderin' round looking this frail..
    take this. 

    He hands you a potion simply labelled 'Vitalis'""")
respond_(["yes", "ok", "okay", "sure", "alright", "yeah", "y", "yea"], 
            "Will you drink the potion?    ")
if tick == 1:
    healthInitial += 20
    windowFunction.Text_("""    Mate, how does that feel, electrifying, eh?
    You'll be able to absorb whatever comes your way now.""")
    windowFunction.typeSlow_("  HEALTH NOW PERMANENTLY INCREASED BY 20!")
else:
    windowFunction.Text_("""    You decide to turn down the potion

    who knows what you missed out on... """)

windowFunction.Text_("""    Now, go out there and do what you must! 
    I'll be waitin on you!""")
areaLevel_()
#//---------------------------ACT 3 - SUNDOWNING----------------------------//
windowFunction.storySetup_("Michal's Arch - Vesenid", 10)
windowFunction.Text_("""    As you approach the arch you see a large sign
    labelled 'In Honour Of Jop Antoine Lepelaar.'
    You notice that the sign is tightly strung with the twine of jute, meaning
    that you know you have ventured out far enough.

    You further examine the sign. Something seems wrong with it""")
respond_(["yes", "ok", "okay", "sure", "alright", "yeah", "y", "yea"],\
    "Do you pull on the sign?   ")
if tick == 1:
    selfPower += 20
    windowFunction.Text_("""    Pulling on the sign strengthened you!
    +20 POWER!""")
    
windowFunction.Text_("""    You walk further and you enter a bursting city
    filled with vibrancy and colour.
    Beautiful houses, adorned in many punchy styles line the streets
    and hundreds of vendors have their stalls placed on the street,
    selling many assorted foodstuffs and crafts, such as good luck charms,
    gemstones and fruits""")

windowFunction.Text_("""    You begin to walk around the street further and 
    you recognise that the sun is beginning to set.
    The sky begins to fade into a mellow shade of purple and
    the sun slowly pulls down. You watch as people begin
    shutting their stores and begin slowly walking into their homes.

    As of nowhere you look to a wall and see a map.
    a map, which takes you to your goal.""")

windowFunction.Text_("""    You'd have to take a 
    shortcut to get there, but it's
    definitely better than walking for days upon days to reach it.
    The 'shortcut' is having to pass through a forest,
    but not just any forest. A forest which no man has walked out of.""")
windowFunction.storySetup_("Map - Mladav Bolen", 11)
windowFunction.Text_("CURRENTLY VIEWING MAP")
windowFunction.ClearFrame_()
areaLevel_()
#//--------------------------ACT 4: ENTRY INTO HELL-------------------------//
windowFunction.storySetup_("Mladav Bolen", 12)
windowFunction.Text_("""    You are minutes away from fighting the fight.
    You just need to get through one more wave, and freedom is at your grasp.

    All that surrounds you is the air of smoke, flames and stench of war.

    You unsheath your sword for the final time. begin.""")
areaLevel_()
windowFunction.ClearFrame_()
windowFunction.Text_("""    YOU.

    I have been expecting you. I know what you want.
    USELESS GUARDS. USELESS SLAVES. USELESS EVERYTHING.
    But I see your potential. I know what you're capable of,
    and I want to see what you can do.

    Do you want to be useful, be SOMETHING FOR ONCE?
    COME INTO MY HANDS. LET ME NURTURE YOU.""")
respond_(["yes", "ok", "okay", "sure", "alright", "yeah", "y", "yea"], \
    "Do you want to betray everything you have come here for?    ")
if tick == 1:
    windowFunction.Text_("""You decide to do it.
    and you bring him to the top.
    Everything is destroyed.""")
    print("")
    windowFunction.typeVerySlow_("And you have been discarded.")
    losses += 1
    save_apply_()
    print("Restart the game to play again.")
    exit()
else:
    windowFunction.Text_("NO. YOU HAVE TO.")
    respond_(["yes", "ok", "okay", "sure", 
                "alright", "yeah", "y", "yea"], \
    "DO YOU DISCARD EVERYTHING YOU HAVE DONE?    ")
    if tick == 1:
        windowFunction.Text_("""    You decide to do it.
    and you bring him to the top.
    Everything is destroyed.""")
        print("")
        windowFunction.typeVerySlow_("And you have been discarded.")
        losses += 1
        save_apply_()
        print("Restart the game to play again.")
        exit()
    else:
        windowFunction.ClearFrame_()
        windowFunction.Text_("""    fine. FINE.
    YOU WILL FEEL TOTAL REGRET.
    YOU WILL UNDERSTAND WHAT YOU HAVE DONE. WHAT YOU HAVE BROUGHT UPON
    YOURSELF.""")

areaLevel_()
bossBattle = 0
section = 31
level = 9999.0
power = 9999.0
if bossBeat == 1:
    windowFunction.Text_("""
    Sickness. Sickness.
    SICKNESS.
    Lemme lend you into a SECRET.
    YOU WERE MEANT TO BE MY HEIR.
    YOU WERE MEANT TO TAKE MY EMPIRE.
    
    son.""")
    windowFunction.ClearFrame_()
    windowFunction.Text_("""
    Maybe going out to the Field Of Dreams and slaying
    some low level enemies will help you clear your mind.
    
    The past day has been stressful.""")
if bossLoss == 1:
    windowFunction.Text_("""
    Kid put up a fair fight.
    Sad it had to come to this but I've got what I need.""")
    windowFunction.ClearFrame_()
    windowFunction.Text_("""
    You decide to go out to visit the Field Of Dreams
    to take a brisk walk and to kill some enemies for fun.""")

areaLevel_()